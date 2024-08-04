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
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/toddleranalogy.png" alt="Toddler Analogy">
    <figcaption>This figure shows the analogy of agents' trajectories to toddlers' learning. (a) Learning trajectory of a toddler. On the left, a toddler's free exploration of an environment represents learning with sparse rewards. On the right, the toddler grows up, she tends to direct their journey towards specific objects, which signify goal-directed learning. Similarly, the agent's journey from sparse rewards to potential-based dense rewards is depicted by the arrow above, drawing a parallel between the learning processes of toddlers and agents.

(b) Summary of baseline rewards. Sparse rewards are only given when agents reach a target. In contrast, potential-based dense rewards are provided based on the agent's proximity to a target object, mimicking the reward transition observed in toddler learning.</figcaption>
</figure>

## Experiments
<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/natureenv.png" alt="Toddler Analogy">
    <figcaption>Performance and sharpness metrics were measured over at least six trials in each environment. Reduced sharpness indicates wide minima, which may improve generalization performance. The best performance and corresponding sharpness values are highlighted in bold, showing that the top-performing \textbf{S2D} also achieves the widest minima. Through ablation studies of the reward transition timing, we found that the optimal reward transition timing occurs within the first third of training, similar to toddlers' critical learning period.</figcaption>
</figure>

## Results
<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/naturemainfigv1.png" alt="Toddler Analogy">
    <figcaption>(a). Performance of the agent with various reward types in multiple goal-oriented tasks. (1-3) Notably, in LunarLander, the accumulated reward from intrinsic rewards was significantly below zero, indicated by a dashed line. We also note that for UR5, both intrinsic motivation and sparse reward settings result in near-zero performance, making it difficult to observe. (4),(5): Generalization performance of the ViZDoom agent with various types of rewards. (b). Performance analysis of agents using different reward strategies in the Toddler Playroom maze environment. (1) and (2) Number of episodes completed over time, showing S2D agents complete more episodes. (3-6) Success rates at different starting points, illustrating higher success rates for S2D agents compared to other baselines. The results highlight the robustness and effectiveness of the S2D transition in complex, visually rich environments mimicking a real toddler's playroom.</figcaption>
</figure>

<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/nature-mainfigv2.png" alt="Toddler Analogy">
    <figcaption>Performance analysis of agents using different reward strategies in the Cross Map maze environment. (a) Episode length during training and evaluation for Goal Points 0, 1, and 2. Agents using the S2D reward transition consistently achieve shorter episode lengths compared to other baselines, indicating more efficient learning. (b) Number of episodes completed and success rates for training and evaluation phases at different goal points. S2D agents display higher sample efficiency and success rates across all scenarios, demonstrating superior performance and generalization to unseen goal positions.</figcaption>
</figure>

## Analysis
<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/natureanalysis.png" alt="Toddler Analogy">
    <figcaption>Visualizations of the trajectories near the final episode and feature analysis in maze environments.
(a) Toddler Playroom Maze Trajectories: The top row displays the exploration paths of agents with different reward settings. S2D and Only Sparse reward agents exhibit diverse, exploratory trajectories, providing opportunities to robustly learn about the environment and objects from various angles. In contrast, Dense reward agents show more straight trajectories, indicating limited exploration patterns and focusing on reaching the goal quickly. The bottom row illustrates the most frequent shortest paths, with S2D agents demonstrating more efficient and direct trajectories to the goal.
(b) Cross Maze Trajectories: Most frequent shortest paths are displayed. We observe patterns similar to those in Toddler Playroom maze, with S2D agents achieving shorter paths compared to other reward settings.
(c) RNN Feature and Action Analysis: The left graph shows the mean distance between RNN features during training, where the reward transition occurs at 3M steps. When observing the region highlighted in red, where features converge notably quickly even compared to Only Dense rewards, it suggests that learning with sparse rewards initially provides good initial parameter points. The right plots depict action distributions (straight, left, right) where predominantly S2D agents maintain stable action patterns after transition, highlighting better policy stability and control. The reward transition occurred at the 300, and the plots are obtained across more than five trials.</figcaption>
</figure>