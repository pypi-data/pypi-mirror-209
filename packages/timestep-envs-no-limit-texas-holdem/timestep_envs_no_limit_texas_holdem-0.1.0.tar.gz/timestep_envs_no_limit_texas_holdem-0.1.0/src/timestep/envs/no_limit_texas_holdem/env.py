from langchain.chat_models import ChatOpenAI

from timestep.agents.action_mask_agent.agent import ActionMaskAgent

def texas_holdem_no_limit(openai_api_key):
    from pettingzoo.classic import texas_holdem_no_limit_v6

    env = texas_holdem_no_limit_v6.env(num_players=4, render_mode="human")
    agents = {
        name: ActionMaskAgent(name=name, model=ChatOpenAI(openai_api_key=openai_api_key, temperature=0.2), env=env)
        for name in env.possible_agents
    }

    return env, agents
