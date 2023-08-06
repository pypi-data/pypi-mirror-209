"""
- Title:            LLM-based Assistants.
- Project/Topic:    Smart Data Science. Practical functions for Data Science  (side project)
- Author/s:         Angel Martinez-Tenor
- Dev Date:         2023

- Status:           In progress.
"""

from __future__ import annotations

import io
import os
import re
from dataclasses import dataclass
from typing import Any

import openai
import pandas as pd
from dotenv import load_dotenv
from IPython.display import Markdown, display
from plotly.graph_objects import Figure

from smart_data_science import logger

log = logger.get_logger(__name__)

# import Any


DEFAULT_TEMPERATURE = 0
TIMEOUT_CODE = 40  # seconds
TIMEOUT_TEXT = 40  # seconds

GLOBAL_DIRECTIVES = {
    "base": "You are a helpful assistant that only focus in solve the user request. ",
    "code_role": "You only returns Python code with no comments or further explanations. \
        All the code generated must be formatted in markdown. \
        No harmful code nor file modification is allowed. ",
    "text_role": "You only returns a text with a short explanation or analysis to the user request. \
        No harmful/hateful commentary or opinion is allowed. ",
}

SPECIFIC_DIRECTIVES = {
    "plot": "The code must generate a plot in plotly and save it in the variable `fig` (do not show it). \
        If the user request is not related to plotting, return a message 'No plot related question",
    "process_data": "The code generated must process the input data and save the result in the variable `df_result`. \
        In case that the user request is not related to dataframe modification, preparation or processing \
        return a message 'No processing-related question",
    "context_analysis": "The text generated must answer the user request with a very short summary, \
    explanation or analysis based on all the context provided. No code generated.",
    "guided_workflow": "The code generated must follow the workflow instructions provided strictly",
}


def pandas_info_to_string(df: pd.DataFrame) -> str:
    """
    Convert the output of df.info() to a string
    Args:
        df: Dataframe to get the info from
    Returns:
        String with the info
    """
    buffer = io.StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()


@dataclass
class HybridAssistant:
    """
    Supervised and OpenAI-based assistant. It generates Python code to solve the user request
    """

    df: pd.DataFrame = None  # Dataframe with the data to process, analyze, plot....
    api_key: str = None  # OpenAI API key, if None, it is read from the .env file
    model = "gpt-3.5-turbo"
    topic_context: str = None  # Topic context for the LLM model
    data_context: dict | str = None  # Dataframe context
    default_temperature = DEFAULT_TEMPERATURE  # default temperature for the OpenAI model (0= deterministic, 1= random)

    def __post_init__(self) -> None:
        """Post initialization"""
        if self.api_key is None:
            load_dotenv()
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key is None:
                raise ValueError("OPENAI_API_KEY not provided nor found in .env file")
            openai.api_key = os.getenv("OPENAI_API_KEY")

        if self.df is not None:
            self.generate_data_context(self.df)

        self.role = {}

        self.role["base"] = GLOBAL_DIRECTIVES["base"]
        self.role["code"] = self.role["base"] + GLOBAL_DIRECTIVES["code_role"]
        self.role["text"] = self.role["base"] + GLOBAL_DIRECTIVES["text_role"]

        self.role["plot"] = self.role["code"] + SPECIFIC_DIRECTIVES["plot"]
        self.role["process_data"] = self.role["code"] + SPECIFIC_DIRECTIVES["process_data"]
        self.role["context_analysis"] = self.role["text"] + SPECIFIC_DIRECTIVES["context_analysis"]
        self.role["guided_workflow"] = self.role["code"] + SPECIFIC_DIRECTIVES["guided_workflow"]

    def set_topic_context(self, text: str) -> None:
        """
        Set the topic context for the OpenAI model
        Args:
            text: Topic context
        """
        self.topic_context = text

    def set_data(self, df: pd.DataFrame) -> None:
        """
        Set the data to process, analyze, plot...
        Args:
            df: Dataframe with the data
        """
        self.df = df
        self.generate_data_context(df)

    def set_data_context(self, custom_context: str | dict) -> None:
        """
        Directly Set the data context for the LLM model
        """
        self.data_context = custom_context

    def generate_data_context(self, df: pd.DataFrame) -> None:
        """
        Automatically Generate the data context for the OpenAI model
        Args:
            df: Dataframe with the data
        Returns:
            Data context
        """
        data_context = {}

        if df is not None:
            data_context["Header"] = df.head(5)
            data_context["Info"] = pandas_info_to_string(df)
            data_context["Description"] = df.describe()

        self.data_context = data_context

    def generate_request_messages(  # depends on LLM model
        self,
        system_role: str,
        user_request: str,
        workflow_instructions: str,
        topic_context: str,
        data_context: str | dict,
        show_request: bool = False,
    ) -> list[dict[str, str]] | str:
        """
        Generate the messages to send to the OpenAI model
        Args:
            system_role: System role
            user_request: User request
            workflow_instructions: Specific instructions
            topic_context: Topic context
            data_context: Data context
            show_request: If True, show the request
        Returns:
            List of messages (OpenAI format)
        """
        if self.model == "gpt-3.5-turbo":
            messages = [{"role": "system", "content": system_role}]

            # messages += [{"role": "user", "content": f"User request (IMPORTANT): {user_request}"}]

            messages += [{"role": "user", "content": f"Workflow instructions: {workflow_instructions}"}]

            if topic_context:
                messages += [{"role": "user", "content": f"Info about Topic/Problem: {topic_context}"}]

            if data_context:
                messages += [{"role": "user", "content": f"Info about data df: {data_context}"}]

            # user request
            messages += [{"role": "user", "content": f"User request (IMPORTANT GOAL TO FOCUS): {user_request}"}]
        elif self.model == "gcp_basic_prompt":
            messages = f"""
                       Role: {system_role}
                      Workflow instructions: {workflow_instructions}
                      Info about Topic/Problem: {topic_context}
                      """
        # TODO Add other LLM models
        else:
            log.critical(f"Model {self.model} not supported yet")
            return None

        if show_request:
            log.info(messages)
            display(messages)
        return messages

    def send_request(self, messages: list | str, timeout: int = None) -> str:
        """
        Send the request to the OpenAI model
        Args:
            messages: List of messages (OpenAI format)
            timeout: Timeout for the request (s)
        Returns:
            Response from the OpenAI model
        """
        if timeout is None:
            timeout = TIMEOUT_TEXT
        log.debug(f"Sending request to LLM model with timeout {timeout} s")
        if self.model == "gpt-3.5-turbo":
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.default_temperature,
                    request_timeout=timeout,
                )
            except openai.error.Timeout:
                log.critical("Timeout error")
        elif self.model == "gcp_basic_prompt":  # TODO 
            return None
        else:
            log.critical(f"Model {self.model} not supported yet")
            return None

        text = response.choices[0]["message"]["content"]
        return text

    def perform_request(
        self,
        system_role: str,
        user_request: str,
        type_request: str = "text",
        workflow_instructions: str = None,
        df: pd.DataFrame = None,
        data_context: str | dict = None,
        topic_context: str = None,
        show_code: bool = False,
        show_request: bool = False,
    ) -> str:
        """
        Code assistant based on GPT-3.5-turbo model. It generates Python code to solve the user request.
        Args:
            system_role: Role of the LLM Model
            user_request: User request to solve
            type_request: Type of request: text or code
            workflow_instructions: Specific instructions for the LLM model
            df: Dataframe with the data to process, analyze, plot....
            data_context: Dataframe context
            topic_context: Topic context for the LLM model
            show_code: If True, the generated code is shown
            show_request: If True, the request is shown
        Returns:
            Generated code (Markdown string)
        """
        if df is None:
            df = self.df.copy()
        else:
            log.info("Dataframe provided, saving data and generating data context")
            self.set_data(df)
            self.generate_data_context(df)

        if data_context is None:
            data_context = self.data_context

        if topic_context is None:
            topic_context = self.topic_context

        messages = self.generate_request_messages(
            system_role, user_request, workflow_instructions, topic_context, data_context, show_request
        )

        # 2 - Send Request to LLM model
        if type_request == "code":
            timeout = TIMEOUT_CODE
        else:
            timeout = TIMEOUT_TEXT
        assistant_text = self.send_request(messages, timeout)

        # 3 -Parse and execute the code generated
        if assistant_text is None:
            return None

        if type_request == "code" and show_code:
            log.info("Code Generated:")
            log.info(assistant_text)
            display(Markdown(assistant_text))

        return assistant_text

    def extract_and_execute_assistant_code(
        self, assistant_text: str, df: pd.DataFrame = None, input_objects: dict = None
    ) -> dict[str, Any] | None:
        """
        Extract the code generated by the assistant and execute it
        Args:
            assistant_text: Text generated by the assistant
            df: Dataframe with the data (basic assistant)
            input_objects: Dictionary with the input objects (guided workflow assistant)
        Returns:
            Dictionary with the variables extracted from the code
        """

        # execute assistant-generated code
        if assistant_text is None:
            return None

        if input_objects is not None:
            log.debug("Input objects provided, using guided workflow assistant")
        elif df is None:
            df = self.df.copy()
            log.debug("No input objects provided and No dataframe provided, using basic assistant with default df")

        # display(assistant_text)

        matches = re.findall("```(?:python)?\n(.*)\n```", assistant_text, re.DOTALL)
        local_variables = locals()
        # display(local_variables.keys())
        returned_text = None
        if len(matches) > 0:
            returned_text = matches[0]
            # Execute the Python code and extract the target variables
            try:
                exec(returned_text, globals(), local_variables)  # pylint: disable=exec-used
            except Exception as e:  # pylint: disable=broad-exception-caught
                log.warning(f"Error executing the code: {e}")
            # else:
            #     log.warning("No code block found in the text")
        return local_variables

    def request_plot(
        self,
        user_request: str,
        df: pd.DataFrame = None,
        data_context: str | dict = None,
        topic_context: str = None,
        show_result: bool = False,
        show_code: bool = False,
        show_request: bool = False,
    ) -> Figure:
        """
        Plotter assistant based on GPT-3.5-turbo model. It generates Python code to plot the data in the dataframe `df`.
        The code is generated based on the user_request and the context provided.
        The context is the dataframe `df` and the problem context.
        The problem context is the problem description and the data source. The user_request is the user
        request to plot the data.
        Args:
            user_request: User request to plot the data.
            df: Dataframe with the data to plot.
            data_context: Dataframe context.
            topic_context: Topic context for the LLM model.
            show_result: If True, the plot is shown.
            show_code: If True, the generated code is shown.
            show_request: If True, the request is shown.
        Returns:
            Plotly Figure with the plot
        """

        # 1 - Prepare the request
        system_role = self.role["plot"]
        specific_instructions = "The input dataframe is 'df', the predictions, is any goes into the column 'predicted'"
        type_request = "code"

        # 2 - Request the code
        assistant_text = self.perform_request(
            system_role,
            user_request,
            type_request,
            specific_instructions,
            df,
            data_context,
            topic_context,
            show_code,
            show_request,
        )
        if assistant_text is None:
            log.warning(f"No code generated: {assistant_text}")
            return None

        # 3 -Parse and execute the code generated
        returned_variables = self.extract_and_execute_assistant_code(assistant_text, df)

        # 4 -Return the plot
        fig = returned_variables.get("fig", None)
        if fig is not None:
            log.info("Figure generated and saved in variable `fig`")
            if show_result:
                fig.show()
            return fig

        log.warning(f"No figure generated: {assistant_text}")
        return None

    def request_process_data(
        self,
        user_request: str,
        df: pd.DataFrame = None,
        data_context: str | dict = None,
        topic_context: str = None,
        show_result: bool = False,
        show_code: bool = False,
        show_request: bool = False,
    ) -> pd.DataFrame:
        """
        Data Processor assistant based on GPT-3.5-turbo model.
        Args:
            user_request: User request to plot the data.
            data: Dataframe with the data to plot.
            data_context: Dataframe context.
            topic_context: Topic context for the LLM model.
            show_result: If True, the plot is shown.
            show_code: If True, the generated code is shown.
            show_request: If True, the request is shown.
        Returns:
            Dataframe with the processed data
        """

        # 1 - Prepare the request
        system_role = self.role["process_data"]
        specific_instructions = "The input dataframe is 'df', the predictions, is any goes into the column 'predicted'"
        type_request = "code"

        # 2 - Request the code
        assistant_text = self.perform_request(
            system_role,
            user_request,
            type_request,
            specific_instructions,
            df,
            data_context,
            topic_context,
            show_code,
            show_request,
        )
        if assistant_text is None:
            log.warning(f"No result generated: {assistant_text}")
            return None

        # 3 -Parse and execute the code generated
        returned_variables = self.extract_and_execute_assistant_code(assistant_text, df)

        # else:
        #     log.warning("No code block found in the text")

        # 4 -Return the dataframe
        df_result = returned_variables.get("df_result", None)
        if df_result is not None:
            log.info("Result generated and saved in the variable 'df_result'")
            if show_result:
                display(df_result)
            return df_result

        log.warning(f"No Processed Data: {assistant_text}")
        return None

    def request_context_analysis(
        self,
        user_request: str,
        df: pd.DataFrame = None,
        data_context: str | dict = None,
        topic_context: str = None,
        show_result: bool = False,
        show_code: bool = False,
        show_request: bool = False,
    ) -> str:
        """
        Context Analysis assistant based on GPT-3.5-turbo model.
        Args:
            user_request: User request to plot the data.
            data: Dataframe with the data to plot.
            data_context: Dataframe context.
            topic_context: Topic context for the LLM model.
            show_result: If True, the plot is shown.
            show_code: If True, the generated code is shown.
            show_request: If True, the request is shown.
        Returns:
            Text with the context analysis requested
        """

        # 1 - Prepare the request
        system_role = self.role["context_analysis"]
        specific_instructions = "The input dataframe is 'df', the predictions, is any goes into the column 'predicted'"
        type_request = "text"

        # 2 - Request the code
        assistant_text = self.perform_request(
            system_role,
            user_request,
            type_request,
            specific_instructions,
            df,
            data_context,
            topic_context,
            show_code,
            show_request,
        )
        if assistant_text is None:
            log.warning(f"No context analysis generated: {assistant_text}")
            return None

        if show_result:
            display(assistant_text)
        return assistant_text

    def request_guided_workflow(
        self,
        user_request: str,
        workflow_instructions: str,
        data_context: str | dict = None,
        topic_context: str = None,
        input_objects: dict = None,
        debug: bool = False,
    ) -> dict:
        """
        Data Processor assistant based on GPT-3.5-turbo model.
        Args:
            user_request: User request to plot the data.
            workflow_instructions: Workflow context.
            data_context: Data (summaries) and context.
            input_objects: Input objects required to execute the workflow.
            debug: If True, the debug mode is activated.
        Returns:
            Dataframe with the processed data
        """

        # 1 - Prepare the request
        system_role = self.role["guided_workflow"]
        type_request = "code"

        # 2 - Request the code
        assistant_text = self.perform_request(
            system_role=system_role,
            user_request=user_request,
            type_request=type_request,
            workflow_instructions=workflow_instructions,
            data_context=data_context,
            topic_context=topic_context,
            show_code=debug,
            show_request=debug,
        )
        if assistant_text is None:
            log.warning(f"No result generated: {assistant_text}")
            return None

        # 3 -Parse and execute the code generated
        returned_variables = self.extract_and_execute_assistant_code(assistant_text, input_objects=input_objects)

        # else:
        #     log.warning("No code block found in the text")

        # 4 -Return the result
        # df_result = returned_variables.get("df_result", None)
        # if df_result is not None:
        #     log.info("Result generated and saved in the variable 'df_result'")
        #     if debug:
        #         log.debug("Result:")
        #         display(df_result)
        #     return df_result
        if returned_variables is not None:
            log.debug("Result generated and saved in the variable 'returned_variables'")
            # if debug:
            #     log.debug("Result:")
            #     display(returned_variables)
            return returned_variables

        log.warning(f"No Processed Data: {assistant_text}")
        return None


# def request_process(request, df=None, data_context=None, problem_context=None, show_output=True):
#     df = df.copy()

#     system_role = "You are a helpful assistant that only returns Python code with no comments or explanations \
#         that solves the user request. The input dataframe is 'df', the prediction, \
#         if any, goes into the column 'predicted'. Always save the processed dataframe in 'df_result' (do not show it)\
#         . No harmful code nor file modification is allowed \
#         If the request is not related to data processing, return a message 'No Data Processing question"

#     if data_context is None and df is not None:
#         data_context = f"Header of df': {df.head(5)}"  #  default context
#         # display(data_context["df"])
#     messages = [{"role": "system", "content": system_role}]

#     if data_context is not None:
#         messages += [{"role": "user", "content": f"Info about data df: {data_context}"}]
#     if problem_context is not None:
#         messages += [{"role": "user", "content": f"Info about problem: {problem_context}"}]

#     messages += [{"role": "user", "content": f"Request: {request}"}]

#     # display(messages)

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         temperature=0.05,
#     )
#     text = response.choices[0]["message"]["content"]

#     log.info("Code Generated:")
#     display(Markdown(text))

#     matches = re.findall("```(?:python)?\n(.*)\n```", text, re.DOTALL)

#     loc = locals()

#     if len(matches) > 0:
#         python_code = matches[0]
#         # Execute the Python code and extract the target variables
#         exec(python_code, globals(), loc)
#     else:
#         log.info("No code block found in the text")

#     if "df_result" in loc:
#         log.info("result generated and saved in the variable `df_result`")
#         if show_output:
#           display(loc.get("df_result", None))
#     return loc
