# MultiAgent demo

## Overview
This repository showcases a collaborative framework using CrewAI to efficiently manage tasks among multiple agents. The project provides an organized structure to leverage CrewAI's capabilities, agents, tasks, and configurations. The modular architecture enables easy scalability and facilitates the addition of new functionalities or agents in the future.

## Features

### 1. CrewAI Implementation
- **Crew Management:** Demonstrates the setup and execution of a Crew using the CrewAI framework.
- **Agent Allocation:** Defines various agents, their roles, goals, and tools for task execution.
- **Task Assignment:** Provides examples of tasks delegated to different agents within the CrewAI framework.

### 2. Agent and OpenAIWrapper Integration
- **Agent Creation:** Illustrates the creation of agents with specific roles and objectives.
- **OpenAI Integration:** Shows integration with the OpenAIWrapper for specific agent tasks.
   
### Running the Code
1. Navigate to the project directory.
2. Execute the main file or specific modules:
    ```bash
    python main.py
    ```

## Configuration

### Agents
- **Researcher Agent (`researcher`):**
    - Role: Senior Research Analyst
    - Objective: Utilizes DuckDuckGo search for in-depth research on user queries.

- **Writer Agent (`writer`):**
    - Role: Tech Content Strategist
    - Objective: Generates blog posts using data collected by the Researcher Agent.

### Tasks
- Tasks are defined in the `tasks.py` file, outlining specific objectives for agents.
