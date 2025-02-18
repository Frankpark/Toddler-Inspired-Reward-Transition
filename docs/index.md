# Toddler 👶 inspired reward transition

## Abstract

Reinforcement learning (RL) agents often face challenges in balancing exploration and exploitation, particularly in environments where sparse or dense rewards bias learning. Biological systems, such as human toddlers, naturally navigate this balance by transitioning from free exploration with sparse rewards to goal-directed behavior guided by increasingly dense rewards. Inspired by this natural progression, we investigate the **Toddler-Inspired Reward Transition** in goal-oriented RL tasks. Our study focuses on *transitioning from sparse to potential-based dense (S2D) rewards* while preserving optimal strategies. Through experiments on dynamic robotic arm manipulation and egocentric 3D navigation tasks, we demonstrate that effective S2D reward transitions significantly enhance learning performance and sample efficiency. Additionally, using a Cross-Density Visualizer, we show that S2D transitions smooth the policy loss landscape, resulting in wider minima that improve generalization in RL models. In addition, we reinterpret Tolman’s maze experiments, underscoring the critical role of early free exploratory learning in the context of S2D rewards. 

## Exemplar Egocentric Videos (Corresponds to Trajectories After Training Completion)

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

.warning {
    color: red;
    font-weight: bold;
    text-align: center;
    margin: 20px;
}

.toggle-button {
    display: flex;
    justify-content: center;
    margin: 10px;
}

.toggle-button button {
    padding: 10px 20px;
    font-size: 16px;
}
</style>

<div class="warning">
        <p>Warning: The D2S video contains flashing lights that may trigger photosensitive seizures.</p>
</div>

<div class="toggle-button">
    <button onclick="toggleD2SVideo()">Toggle D2S Video</button>
</div>

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
    <figure id="d2s-video" style="margin: 5px; display: none;">
        <video width="200" autoplay loop muted>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-d2s.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <figcaption><center>D2S</center></figcaption>
    </figure>

<script>
function toggleD2SVideo() {
    const d2sVideo = document.getElementById('d2s-video');
    if (d2sVideo.style.display === 'none') {
        d2sVideo.style.display = 'block';
    } else {
        d2sVideo.style.display = 'none';
    }
}
</script>
</div>

## Trajectory Videos (Most Common Cases After Training Completion - Corresponding to Exemplar Videos)
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

<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/natureanalysis_diverse.png" alt="Diverse trajectories">
    <figcaption>
    <center>
    The trajectory videos (final behavior) show that <bold>S2D agents</bold> eventually take the shortest and most direct paths to the goal, balancing exploration and exploitation. Early in training, they exhibit diverse, exploratory paths similar to sparse-only agents. In contrast, <bold>dense-only agents</bold> display rigid, straight-line behaviors even in the early stages of training. This leads to less exploration and a limited understanding of the environment. S2D agents, however, actively explore in the early stages, which enables them to transition into more efficient and goal-oriented behavior as dense rewards guide their trajectories later in training.
    </center>
    </figcaption>
</figure>


## Key findings
- Transitioning from sparse-to-dense reward significantly improves learning outcomes, balancing exploration and exploitation to enhance success rates and sample efficiency.

- The S2D reward transition smooths the policy loss landscape, promoting wider minima and enhancing generalization.

- Agents' free exploration during the sparse reward phase forms good initial policy parameters, leading to more stable and faster learning when transitioning to dense rewards.

- We developed custom 3D environments for egocentric scenarios, including ViZDoom and the minecraft mazes, specialized for generalization measures.

## Reward transition inspired by toddlers

<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/toddleranalogy.png" alt="A picture of a toddler room and its sparse, dense reward zone">
    <figcaption>
    Analogy of agents' trajectories to toddlers' learning. (a) Learning trajectory of a toddler. On the left, a toddler's free exploration of an environment represents learning with sparse rewards. On the right, the toddler grows up, she tends to direct their journey towards specific objects, which signifies goal-directed learning. Similarly, the agent's journey from sparse rewards to potential-based dense rewards is depicted by the arrow above, drawing a parallel between the learning processes of toddlers and agents. (b) Summary of baseline rewards. Sparse rewards are only given when agents reach a target. In contrast, potential-based dense rewards are provided based on the agent's proximity to a target object, mimicking the reward transition observed in toddler learning. 
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
    Experimental environments and policy loss landscape analysis. (a) ViZDoom environments: ViZDoom-Seen features familiar wall textures, while ViZDoom-Unseen randomly chooses among three new wall textures, requiring agents to adapt to unseen backgrounds. (b) Minecraft environments: In the Cross Maze, one goal point (0, 1, or 2) is not selected during training, and the agent's generalization is evaluated across all positions. Toddler Playroom Maze with four spawn points and a goal randomly appearing in the red zone. In this environment, agents must learn through egocentric image observations that include objects of various sizes and colors, providing diverse representations. (c) Additional environments: modified UR5-Reacher, Cartpole-Reacher with randomly spawned goals and the detailed description of the LunarLander is detailed in appendix A. (d) Analysis of policy loss landscape after reward transition: The 3D visualization depicts the policy loss landscape following a reward transition, which begins with either a sparse or dense reward. The upper row shows dense-to-dense (Only Dense) and dense-to-sparse (D2S) transitions, and the lower row shows sparse-to-dense (S2D) and sparse-to-sparse (Only Sparse) transitions. Significant smoothing effects were primarily observed during the S2D transition, helping to overcome local minima and fostering wider minima, which enhance generalization. These effects were evident following the transition at $T=50$ and $T=2000$ in LunarLander, and at $T=3500$ in Cartpole-Reacher. Detailed 3D visualizations can be found in Appendix B.</figcaption>
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
    (a). The agent's performance across different reward schemes in several goal-driven tasks. (1-3) Interestingly, in LunarLander, the total reward gained from intrinsic incentives was well below zero, as shown by the dashed line. We also note that for UR5, both intrinsic motivation and sparse reward settings result in near-zero performance, making it difficult to observe. (4), (5): The ViZDoom agent's ability to generalize across different reward types. (b). Performance analysis of agents using different reward strategies in the Toddler Playroom maze environment. (1) and (2) Number of episodes completed over time, showing S2D agents complete more episodes. (3-6) Success rates at different starting points, illustrating higher success rates for S2D agents compared to other baselines. The results highlight the robustness and effectiveness of the S2D transition in complex, visually rich environments mimicking a real toddler's playroom.
    </figcaption>
</figure>

The results of our experiments demonstrate the efficacy of the S2D (Sparse to Dense) reward transition strategy across various goal-oriented tasks and environments.

### Performance in Goal-Oriented Tasks
- **LunarLander**: The accumulated reward from intrinsic rewards was significantly below zero, as indicated by the dashed line, highlighting the challenges with intrinsic rewards alone.
- **CartPole**: S2D agents showed a clear advantage, outperforming other reward strategies in terms of success rate. Although intrinsic rewards exhibited comparable performance to S2D during early exploration, S2D ultimately led to more consistent performance gains.
- **UR5**: Both intrinsic motivation and sparse reward settings resulted in near-zero performance, making it challenging to observe substantial learning.
- **ViZDoom**: The generalization performance of agents was evaluated with various reward types, showing that S2D transitions lead to better generalization compared to other strategies.

### Performance in the Toddler Playroom Maze Environment
- **Number of Episodes Completed**: S2D agents completed more episodes over time compared to other reward strategies.
- **Success Rates**: Higher success rates were observed for S2D agents at different starting points, illustrating the robustness and effectiveness of the S2D transition in complex, visually rich environments mimicking a toddler's playroom.


<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/naturemainfigV2.png" alt="Graphs of episode length and episode reached per global steps">
    <figcaption>
    Performance analysis of agents using different reward strategies in the Cross maze environment. (a) Episode length during training and evaluation for Goal Points 0, 1, and 2. Agents using the S2D transition consistently achieve shorter episode lengths compared to other baselines, indicating more efficient learning. (b) Number of episodes completed and success rates for training and evaluation phases at different goal points. S2D agents display higher sample efficiency and success rates across all scenarios, demonstrating superior performance and generalization to unseen goal positions.
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
    Visualizations of the trajectories near the final episode and feature analysis in maze environments. (a) Toddler Playroom Maze Trajectories: The top row displays the exploration paths of agents with different reward settings. S2D and Only Sparse agents exhibit diverse, exploratory trajectories, providing opportunities to robustly learn about the environment and objects from various angles. In contrast, Only Dense agents show more straight trajectories, indicating limited exploration patterns and focusing on reaching the goal quickly. The bottom row illustrates the most frequent shortest paths, with S2D agents demonstrating more efficient and direct trajectories to the goal. (b) Cross Maze Trajectories: Most frequent shortest paths are displayed. We observe patterns similar to those in Toddler Playroom maze, with S2D agents achieving shorter paths compared to other reward settings. (c) RNN Feature and Action Analysis: The left graph shows the mean distance between RNN features during training, where the reward transition occurs at 3M steps. In the region highlighted in red, the features converge notably quickly for S2D even compared to Only Dense, which suggests that learning with sparse rewards initially provides good initial parameter points. The right plots depict action distributions (straight, left, right) where predominantly S2D agents maintain stable action patterns after transition, highlighting better policy stability and control. The reward transition occurred at the 3M, and the plots are obtained across more than five trials.
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
