# Toddler 👶 inspired reward transition

## Abstract

Consider the journey of toddlers: they progress from free exploration with sparse feedback to goal-directed learning with denser rewards. Inspired by this phenomenon, we aim to explore the <b>Toddler-Inspired Reward Transition</b> in goal-oriented reinforcement learning (RL) tasks. Our primary focus is on <i>transitioning from sparse to potential-based dense (S2D) rewards</i> while maintaining optimal strategies. Through a series of experiments, including dynamic robotic arm manipulation tasks and egocentric 3D navigation tasks, our results show that proper S2D reward transitions are key to enhancing learning performance and sample efficiency, thereby balancing exploration and exploitation more effectively. As part of our analysis, we offer a novel interpretation of Tolman's maze experiments, emphasizing the importance of free exploratory learning in the initial stages. Furthermore, using our Cross-Density Visualizer. we discover that S2D reward transitions smooth the policy loss landscape, promoting wide minima, which significantly enhances generalization.

## Exemplar Egocentric Videos

<style>
.styled-figure {
    text-align: center;
    margin: 20px;
}

figcaption {
    font-style: italic;
    color: gray;
    font-size: 12px;
    margin-top: 3px;
}
</style>

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
    <figure style="margin: 5px;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-sparse.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>Only Sparse</center></figcaption>
    </figure>
    <figure style="margin: 5px;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-dense-1.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>Only Dense</center></figcaption>
    </figure>
    <figure style="margin: 5px;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-s2d-2.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>S2D</center></figcaption>
    </figure>
    <figure style="margin: 5px;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-d2s.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>D2S</center></figcaption>
    </figure>
</div>

## Trajectory Videos (Most common cases)
<div style="display: flex; flex-wrap: wrap; justify-content: center;">
    <figure style="margin: 5px;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-sparse-traj.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>Only Sparse</center></figcaption>
    </figure>
    <figure style="margin: 5px;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-dense-1-traj.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>Only Dense</center></figcaption>
    </figure>
    <figure style="margin: 5px;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-s2d-2-traj.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>S2D</center></figcaption>
    </figure>
    <figure style="margin: 5px;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-d2s-traj.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>D2S</center></figcaption>
    </figure>
</div>

## Key findings
- Transitioning from sparse-to-dense reward significantly improves learning outcomes, balancing exploration and exploitation to enhance success rates and sample efficiency.

- The S2D reward transition smooths the policy loss landscape, promoting wider minima and enhancing generalization.

- Agents' free exploration during the sparse reward phase forms good initial policy parameters, leading to more stable and faster learning when transitioning to dense rewards.

- We developed custom 3D environments for egocentric scenarios, including ViZDoom and the minecraft mazes, specialized for generalization measures.

## Reward transition inspired by toddlers

<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/toddleranalogy.png" alt="A picture of a toddler room and its sparse, dense reward zone">
    <figcaption>
    (a) Toddlers transition from free exploration (sparse rewards) to goal-directed learning (dense rewards). (b) Agents mimic this by initially receiving sparse rewards, then transitioning to dense rewards based on proximity to the target.
</figcaption>
</figure>
The concept of reward transition in reinforcement learning is inspired by the developmental stages of toddlers. Initially, toddlers engage in free exploration with minimal guidance, representing a phase of learning with sparse rewards. As they grow, their interactions become more goal-directed, similar to learning with dense rewards. This transition from sparse to dense rewards in agents can significantly enhance learning efficiency and performance.

### Learning Trajectory of a Toddler
- **Free Exploration**: At early stages, toddlers explore their environment freely, learning through sparse feedback. This exploration helps them build a broad understanding of their surroundings.

- **Goal-Directed Learning**: As they mature, their activities become more directed towards specific goals, receiving denser rewards for reaching those goals. This stage represents a shift to more focused and efficient learning.

### Agents’ Reward Transition
- **Sparse Rewards**: Agents initially receive rewards only when achieving specific targets, encouraging exploration and diverse learning experiences.

- **Dense Rewards**: Later, agents receive rewards based on their proximity to the target, promoting more direct and efficient learning paths. This mirrors the transition toddlers undergo, optimizing the learning process by balancing exploration and exploitation.


## Experiments
<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/natureenv.png" alt="Pictures of environments">
    <figcaption>
    Performance and sharpness metrics from trials. S2D shows the best performance and widest minima, indicating improved generalization. Optimal reward transition timing is within the first third of training.
</figcaption>
</figure>
In our experiments, we assessed the performance and sharpness metrics across various environments, each trial being conducted at least six times. Sharpness refers to the landscape of the loss function; reduced sharpness often correlates with wide minima, which are desirable for improving generalization performance.

### Performance Metrics
The performance of different reward transition strategies was measured, with S2D (Sparse to Dense) achieving the best results.

### Sharpness Metrics
Sharpness values were evaluated to understand the stability and generalization potential of the learned policies. The S2D approach not only showed superior performance but also the widest minima, indicating a more robust and generalizable learning process.

### Optimal Timing for Reward Transition
Through detailed ablation studies, we determined that the optimal timing for transitioning from sparse to dense rewards is within the first third of the training period. This timing aligns with critical learning periods observed in toddler development, suggesting that early transitions can significantly enhance learning efficiency and outcomes.

## Results
<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/naturemainfigv1.png" alt="Graphs of average reward, success rate, average episode reached, and episode lengths of various environments">
    <figcaption>
    (a) Agent performance with various reward types in goal-oriented tasks. (1-3) LunarLander and UR5 show challenges with intrinsic rewards. (4-5) ViZDoom generalization performance with different rewards. (b) S2D agents in the Toddler Playroom maze show more completed episodes and higher success rates compared to other baselines.
    </figcaption>
</figure>

The results of our experiments demonstrate the efficacy of the S2D (Sparse to Dense) reward transition strategy across various goal-oriented tasks and environments.

### Performance in Goal-Oriented Tasks
- **LunarLander**: The accumulated reward from intrinsic rewards was significantly below zero, as indicated by the dashed line, highlighting the challenges with intrinsic rewards alone.
- **UR5**: Both intrinsic motivation and sparse reward settings resulted in near-zero performance, making it challenging to observe substantial learning.
- **ViZDoom**: The generalization performance of agents was evaluated with various reward types, showing that S2D transitions lead to better generalization compared to other strategies.

### Performance in the Toddler Playroom Maze Environment
- **Number of Episodes Completed**: S2D agents completed more episodes over time compared to other reward strategies.
- **Success Rates**: Higher success rates were observed for S2D agents at different starting points, illustrating the robustness and effectiveness of the S2D transition in complex, visually rich environments mimicking a toddler's playroom.


<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/naturemainfigV2.png" alt="Graphs of episode length and episode reached per global steps">
    <figcaption>
    (a) Episode lengths during training and evaluation for Goal Points 0, 1, and 2, showing more efficient learning with S2D. (b) Number of episodes completed and success rates, with S2D agents displaying superior sample efficiency and generalization across all scenarios.
</figcaption>
</figure>

### Performance in the Cross Map Maze Environment
In our study, we evaluated the performance of agents using different reward strategies in the Cross Map maze environment. The results indicate significant improvements in learning efficiency and generalization for agents using the S2D (Sparse to Dense) reward transition.

- **Episode Length**: For Goal Points 0, 1, and 2, agents that use the S2D reward transition consistently achieved shorter episode lengths compared to other baselines. This indicates that S2D facilitates more efficient learning, allowing agents to complete tasks more quickly.

- **Training Phases**: S2D agents demonstrated higher sample efficiency, completing more episodes within the same training period.

- **Evaluation Phases**: During evaluation, S2D agents achieved higher success rates across all goal points, showcasing superior performance and better generalization to unseen goal positions.

## Analysis

The analysis focuses on the visualizations of agent trajectories and feature analysis in various maze environments. This helps understanding the impact of different reward strategies on agent behavior and learning efficiency.

<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/natureanalysis.png" alt="Trajectory images in toddler room maze and cross maze, and analysis results">
    <figcaption>
    (a) S2D and Sparse agents exhibit diverse trajectories, enhancing learning; Dense agents show straight paths. (b) S2D agents achieve shorter paths in Cross Maze. (c) RNN features converge faster with sparse rewards initially; S2D agents maintain stable actions.
</figcaption>
</figure>

### Toddler Playroom Maze Trajectories
- **Exploration Paths**: In the top row, the trajectories of agents with S2D and Only Sparse rewards are diverse and exploratory, allowing for robust learning about the environment and objects from various angles. Conversely, agents with Dense rewards show more straightforward trajectories, indicating limited exploration and a focus on quickly reaching the goal.

- **Shortest Paths**: The bottom row illustrates the most frequent shortest paths. S2D agents demonstrate more efficient and direct paths to the goal compared to other reward settings.

### Cross Maze Trajectories
Similar to the Toddler Playroom maze, the S2D agents in the Cross Maze achieve shorter and more efficient paths compared to other reward settings, reinforcing the benefits of the S2D strategy.

### RNN Feature and Action Analysis
- **Feature Convergence**: The left graph shows the mean distance between RNN features during training, with a noticeable convergence occurring at the 3 million steps mark, especially in the region highlighted in red. This suggests that initial learning with sparse rewards provides a good foundation for parameter optimization.
- **Action Distributions**: The right plots shows the distribution of actions (straight, left, right) taken by agents. S2D agents maintain stable action patterns after the transition, highlighting improved policy stability and control.


## Supplementary Videos
You can download the supplementary videos from the following links:

- Video 1: Toddler Playroom Maze Trajectories + Ego-centric View
    - [Download Video](https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/s2d-room-movie-speedup.mp4)
- Video 2: Cross Maze Trajectories + Ego-centric View
    - [Download Video](https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/s2d-cross-movie-speedup.mp4)



</figure>