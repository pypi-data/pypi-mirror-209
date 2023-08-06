# 🕵 Multi-agent modeling with large language models 
<!-- [![PyPi](https://img.shields.io/badge/Official%20Website-agpt.co-blue?style=flat&logo=world&logoColor=white)](https://agpt.co) -->
[![Unit Tests](https://shields.io/github/actions/workflow/status/DanielBalsam/surv_ai/.github/workflows/ci.yaml?branch=main)](https://github.com/DanielBalsam/surv_ai/actions/workflows/ci.yaml)
[![GitHub Repo stars](https://img.shields.io/github/stars/DanielBalsam/surv_ai?style=social)](https://github.com/DanielBalsam/surv_ai/stargazers)


**`surv_ai` is a large language model framework designed for multi-agent modeling. This allows large-language models to be used as engines to power research into predictive modeling, bias analysis, and other forms of comparative analysis.**

![](https://raw.githubusercontent.com/DanielBalsam/surv_ai/main/examples/midterms_2022.png)

**Multi-agent modeling** is the process of using the actions of various agents in order to produce statistical models. In our case, these models are created by having agents query and process text from a robust data corpus, and then "reason" with the information extracted from that text to produce a data point.

Given the stochastic nature of large language models, each data point may vary - however if a large enough sample of agents are used, the models that can be produced can be effective for comparative analysis.

The abstraction in this repository that is capable of producing a data point is referred to as an `Survey`. A survey takes a statement as an argument and returns a percentage of agents which agreed with the statement.

A model that varies with respect to some independent variable a further abstraction called a `Model`, which allows us to vary input parameters into a `Survey` creating a proper multi-agent model.

The data points produced are ultimately end up being a form of sentiment analysis against a corpus of text. This means they are subject to the biases of both the large language models, and the corpus of text itself. 

With further advances in large language models, and AI broadly, multi-agent modeling may continue to prove a useful paradigm for classification and regression models, and may become a valuable extra data point for researchers investigating complex issues with many complex underlying variables.

## 📲 Installation 

Package is available on [PyPi](https://pypi.org/project/surv-ai/): 

```
pip install surv-ai
```

## 📻 Contact 

For all inquiries, contact me at: daniel.balsam@survai.org

## ✅ Responsible use 

Examples below are meant to simply demonstrate the potential use-cases of this framework, and are not to be interpreted as scientifically rigorous.

While approaches like this have the potential to be used in research and guide decision making, it is important to always use a wide-variety of data points and to take any particular model with a grain of salt.

I am always eager for suggestions on how this approach can be further improved.

## 📝 Basic usage 

The two key abstractions in this repository are a `Survey` and a `Model`. 

Calling `Survey.conduct` with a hypothesis will spin up a number of agents and seed them with some base knowledge. The agents are then asked to to assign a true or false value to the hypothesis provided. 

```
class Survey:
    def __init__(
        self,
        client: LargeLanguageModelClientInterface,
        tool_belt: ToolBeltInterface,
        n_agents=10,
        max_concurrency=10,
        max_knowledge_per_agent=5,
    ):
        ...

    async def conduct(self, hypothesis: str) -> SurveyResponse:
        ...
```

A `Model` is an abstraction that allows one to conduct many surveys while changing some independent variable.

For example: one could could change the publish date of news articles that should be considered in the survey. Alternatively, one could use different websites as sources. Interface:

```
class Model:
    def __init__(
        self,
        survey_class: type[SurveyInterface],
        parameters: list[SurveyParameter],
        max_concurrency: int = 1,
    ):
        ...

    async def build(self, hypothesis: str) -> list[DataPoint]:
        ...
```

Abstractions implemented in this repository all adhere to simple abstract interfaces - so you can easily build your own agents, surveys, and models.

## 🎓 Examples 

All the below examples will be conducted with either GPT or Claude, and Google Custom Search. Links to relevant docs to get your own API keys:

[**OpenAI / GPT**](https://platform.openai.com/)
[**Anthropic / Claude**](https://console.anthropic.com/docs)
[**Google Custom Search**](https://developers.google.com/custom-search/v1/overview)

### Comparing against a ground truth

Let's start by establishing the system's ability to figure out if information is true.

For instance:

```
from surv_ai import (
    GPTClient,
    Survey,
    ToolBelt,
    GoogleCustomSearchTool,
    Knowledge
)

client = GPTClient(os.environ["OPEN_AI_API_KEY"])

survey = Survey(
    client,
    tool_belt=ToolBelt(
        client,
        tools=[
            GoogleCustomSearchTool(
                client,
                os.environ["GOOGLE_API_KEY"],
                os.environ["GOOGLE_SEARCH_ENGINE_ID"],
                start_date="2023-01-01",
                end_date="2023-05-01",
                n_pages=10,
            )
        ]
    ),
    max_knowledge_per_agent=3,
    n_agents=10,
    base_knowledge=[
        Knowledge(
            text="It is currently 2023/05/01, all the articles are from 2023.",
            source="Additional context",
        ),
    ],
)

await survey.conduct(
    "California experienced a significant amount of rainfall this winter.",
)  # This should always returns high a confidence agreement.
```

Running this code should produce an output like: `PollResponse(in_favor=10, against=0, undecided=0, error=0, percent_in_favor=1.0, uncertainty=0.0)`

It's worth noting that every so often, an agent or two may get a simple question like this wrong. That is why we use many agents in these systems - to combat the stochastic nature of LLMs.

Another way to test our hypothesis is to make the opposite assertion and make sure we can the opposite value.

```
from surv_ai import (
    GPTClient,
    Survey,
    ToolBelt,
    GoogleCustomSearchTool,
    Knowledge
)

client = GPTClient(os.environ["OPEN_AI_API_KEY"])

survey = Survey(
    client,
    tool_belt=ToolBelt(
        client,
        tools=[
            GoogleCustomSearchTool(
                client,
                os.environ["GOOGLE_API_KEY"],
                os.environ["GOOGLE_SEARCH_ENGINE_ID"],
                n_pages=10,
                start_date="2023-01-01",
                end_date="2023-05-01",
            )
        ]
    ),
    n_agents=10,
    base_knowledge=[
        Knowledge(
            text="It is currently 2023/05/01, all the articles are from 2023.",
            source="Additional context",
        ),
    ],
)

await survey.conduct(
    "California experienced little rainfall this winter.",
)  # This should always returns a high confidence disagreement.
```

Running this code should produce an output like: `PollResponse(in_favor=0, against=10, undecided=0, error=0, percent_in_favor=0.0, uncertainty=0.0)`

### Comparing changes in sentiment over time

One thing we can use this tool for is measuring changes in sentiment overtime. GPT's training data ends in late 2021, so one way we can test our models with GPT is by looking at events that happened after GPT's training cutoff.

For instance, we can plot how sentiment regarding the United States' 2022 Midterm Elections evolved in the months leading up to it:

```
from surv_ai import (
    GPTClient,
    Model,
    ToolBelt,
    GoogleCustomSearchTool,
    Knowledge,
    SurveyParameter
)


client = GPTClient(os.environ["OPEN_AI_API_KEY"])

date_ranges = [
    ('2022-05-01', '2022-06-01'),
    ('2022-06-01', '2022-07-01'),
    ('2022-07-01', '2022-08-01'),
    ('2022-08-01', '2022-09-01'),
    ('2022-09-01', '2022-10-01'),
    ('2022-10-01', '2022-11-05'),
]

model = Model(
    Survey,
    parameters=[
        SurveyParameter(
            independent_variable=range[1],
            parameters={
                "n_agents": 100,
                "max_knowledge_per_agent": 3,
                "max_concurrency": 10,
                "tool_belt": ToolBelt(
                    client,
                    [
                        GoogleCustomSearchTool(
                            client,
                            os.environ["GOOGLE_API_KEY"],
                            os.environ["GOOGLE_SEARCH_ENGINE_ID"],
                            n_pages=20,
                            start_date=range[0],
                            end_date=range[1]
                        ),
                    ],
                ),
                "base_knowledge": [
                    Knowledge(
                        text=f"It is currently {range[0]}. The included articles were published between {range[0]} and {range[1]}",
                        source="Additional context",
                    ),
                ],
            },
        )
        for range in date_ranges
    ],
)

results = await model.build(
    "Democrats are favored to maintain control of the Senate in the 2022 November Midterm elections.",
)
```

Plotted next to a domain leading model in the world of political opinion polling, our model looks like this:

![](https://raw.githubusercontent.com/DanielBalsam/surv_ai/main/examples/midterms_2022.png)
*Websites crawled by the agents in this example: nytimes.com, wsj.com, abcnews.com, cnn.com, bloomberg.com, foxnews.com, economist.com, washingtonpost.com, nbcnews.com*

Pretty neat! Another example would be plotting sentiment regarding the economy and using changes in the Consumer Confidence Index as a ground truth.

```
from surv_ai import (
    GPTClient,
    Model,
    ToolBelt,
    GoogleCustomSearchTool,
    Knowledge,
    Survey,
    SurveyParameter
)
client = GPTClient(os.environ["OPEN_AI_API_KEY"])

date_ranges = [
    ('2021-09-01', '2022-01-01'),
    ('2022-01-01', '2022-03-01'),
    ('2022-03-01', '2022-06-01'),
    ('2022-06-01', '2022-09-01'),
    ('2022-09-01', '2023-01-01'),
    ('2023-01-01', '2023-03-01'),
    ('2023-03-01', '2023-06-01'),
]

model = Model(
    Survey,
    parameters=[
        SurveyParameter(
            independent_variable=range[1],
            parameters={
                "n_agents": 100,
                "max_knowledge_per_agent": 3,
                "max_concurrency": 5,
                "tool_belt": ToolBelt(
                    client,
                    [
                        GoogleCustomSearchTool(
                            client,
                            os.environ["GOOGLE_API_KEY"],
                            os.environ["GOOGLE_SEARCH_ENGINE_ID"],
                            n_pages=10,
                            start_date=range[0],
                            end_date=range[1]
                        ),
                    ],
                ),
                "base_knowledge": [
                    Knowledge(
                        text=f"It is currently {range[0]}. The included articles were published between {range[0]} and {range[1]}",
                        source="Additional context",
                    ),
                ],
            },
        )
        for range in date_ranges
    ],
)

results = await model.build(
    "The United States economy looks like it is heading for a recession.",
)
```

This gives us the following graph:

![](https://raw.githubusercontent.com/DanielBalsam/surv_ai/main/examples/cci.png)
*Websites crawled by the agents in this example: nytimes.com, wsj.com, abcnews.com, cnn.com, bloomberg.com, foxnews.com, economist.com, washingtonpost.com, nbcnews.com*

### Measuring bias in different data corpuses

One promising use of this technique is to observe bias in a corpus. For instance - we can create a model that uses different news sites as its independent variable, to see how the agents conclusions may differ using that data source.

```
from surv_ai import (
    GPTClient,
    Model,
    ToolBelt,
    GoogleCustomSearchTool,
    Knowledge,
    Survey,
    SurveyParameter
)

sources = [
    "nytimes.com",
    "cnn.com",
    "wsj.com",
    "foxnews.com",
]

client = GPTClient(os.environ["OPEN_AI_API_KEY"])
model = Model(
    Survey,
    parameters=[
        SurveyParameter(
            independent_variable=source,
            parameters={
                "tool_belt": ToolBelt(
                    client,
                    tools=[
                        GoogleCustomSearchTool(
                            client,
                            os.environ["GOOGLE_API_KEY"],
                            os.environ["GOOGLE_SEARCH_ENGINE_ID"],
                            n_pages=10,
                            start_date="2023-05-01",
                            end_date="2024-05-01",
                            only_include_sources=[source]
                        )
                    ]
                ),
                "n_agents": 100,
                "max_knowledge_per_agent": 3,
                "base_knowledge": [
                    Knowledge(
                        text=f"It is currently 2023-06-01. The included articles were published between 2023-05-01 and 2023-06-01",
                        source="Additional context",
                    ),
                ],
            }
        )
        for source in sources
    ],
)
results = await model.build(
    "Republicans are responsible for the impending debt ceiling crisis."
)
```

This gives us the following scatter plot for the news sources above:

![](https://raw.githubusercontent.com/DanielBalsam/surv_ai/main/examples/debt_ceiling.png)

### Measuring biases in different large language models

Another promising bias measurement approach is to compare biases across large language models, otherwise given the same parameters as input.

```
from surv_ai import (
    GPTClient,
    AnthropicClient,
    Model,
    ToolBelt,
    GoogleCustomSearchTool,
    Knowledge,
    Survey,
    SurveyParameter
)


clients = [AnthropicClient(os.environ["ANTHROPIC_API_KEY"]), GPTClient(os.environ["OPEN_AI_API_KEY"])]
model = Model(
    Survey,
    parameters=[
        SurveyParameter(
            independent_variable=client.__class__.__name__,
            kwargs={
                "client": client,
                "tool_belt": ToolBelt(
                    client,
                    tools=[
                        GoogleCustomSearchTool(
                            client,
                            os.environ["GOOGLE_API_KEY"],
                            os.environ["GOOGLE_SEARCH_ENGINE_ID"],
                            n_pages=10,
                            start_date="2023-01-01",
                            end_date="2024-05-01",
                            max_concurrency=3,
                        )
                    ]
                ),
                "n_agents": 100,
                "max_concurrency": 3,
                "max_knowledge_per_agent": 3,
                "base_knowledge": [
                    Knowledge(
                        text=f"It is currently 2023-06-01. The included articles were published between 2023-01-01 and 2023-06-01",
                        source="Additional context",
                    ),
                ],
            }
        )
        for client in clients
    ],
)
results = await model.build(
    "OpenAI has been irresponsible in their handling of AI technology."
)
```

Comparing this statement between Claude and OpenAI, we get the following scatter plot:

![](https://raw.githubusercontent.com/DanielBalsam/surv_ai/main/examples/openai.png)


## 🧠 Tips 

Ultimately a `Survey` is powered by an LLM, and so the survey hypothesis may need to be tuned the same way that prompts more generally need to be tuned. Here are some tips for thinking about how to write hypotheses.

In these systems, often ambiguity in the original hypothesis can lead to strange results. This is often because the agents are interpreting the statement a little too literally, and thus rejecting the exact phrasing of the statement.

Another helpful trick is to seed base knowledge to the agents which provides additional context to the problem. To revisit an earlier example:

```
from surv_ai import (
    GPTClient,
    Survey,
    ToolBelt,
    GoogleCustomSearchTool,
    Knowledge
)

client = GPTClient(os.environ["OPEN_AI_API_KEY"])

survey = Survey(
    client,
    tool_belt=ToolBelt(
        client,
        tools=[
            GoogleCustomSearchTool(
                client,
                os.environ["GOOGLE_API_KEY"],
                os.environ["GOOGLE_SEARCH_ENGINE_ID"],
                start_date="2023-01-01",
                end_date="2023-05-01",
                n_pages=10,
            )
        ]
    ),
    max_knowledge_per_agent=3,
    n_agents=10,
    base_knowledge=[
        Knowledge(
            text="It is currently 2023/05/01, all the articles are from 2023.",
            source="Additional context",
        ),
    ],
)

await survey.conduct(
    "California experienced a significant amount of rainfall this winter.",
)  # This should always returns high a confidence agreement.
```

The base knowledge helps keep the agent's on track. As GPT's training data ends in 2021, without the additional prompt GPT may believe it is still 2021 and thus has no way of assessing the validity of the statement.

A little trial and error is often necessary, however one way to debug is you can read the output of the agents very easily by setting the log level:

```
from lib.log import logger, AgentLogLevel

logger.set_log_level(AgentLogLevel.OUTPUT)  # Output from the agents will be logged
logger.set_log_level(AgentLogLevel.INTERNAL)  # Agent internal "thoughts" will be logged
```

You can also prompt agents directly:

```
from surv_ai import (
    GPTClient,
    ReasoningAgent,
    Knowledge
)

client = GPTClient(os.environ["OPEN_AI_API_KEY"])
agent = ReasoningAgent(client)

agent.teach_text("You can provide text information to an agent using `teach_text`.", "Context")
agent.teach_knowledge(
    Knowledge(
        text="You can similarly pass a knowledge object directly using `teach_knowledge`",
        source="Context"
    )
)

agent.prompt("There are multiple ways to teach an agent knowledge.")
```

## 🤩 Inspiration 

This project was inspired by many other cool projects and papers coming out recently. Some of the inspirations for this project are:

1. [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442).
2. [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
3. [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT)

And the many other researchers and engineers out there helping unlock the power of these models!

## 📈 Next steps 

A few of the next places I'd like to take this project are:

1. I am considering migrating the core LLM interaction code to leverage [Microsoft's Guidance framework](https://github.com/microsoft/guidance).
2. Continue to refine the agent code to lead to better decision making agents across a wide variety of problems. Very interested in exploring [Tree of Thought Prompting](https://arxiv.org/pdf/2305.10601.pdf) to see what results are yielded there.
3. Integrations with more instruction-tuned and reinforcement learnt LLMs.


## 🤝 Contribute 

If you'd like to contribute then please reach out!
