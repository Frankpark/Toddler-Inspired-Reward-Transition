# Toddler 👶 inspired reward transition

## Abstract

Consider the journey of toddlers: they progress from free exploration with sparse feedback to goal-directed learning with denser rewards. Inspired by this phenomenon, we aim to explore the \textbf{Toddler-Inspired Reward Transition} in goal-oriented reinforcement learning (RL) tasks. Our primary focus is on \textit{transitioning from sparse to potential-based dense (S2D) rewards} while maintaining optimal strategies. Through a series of experiments, including dynamic robotic arm manipulation tasks and egocentric 3D navigation tasks, our results show that proper S2D reward transitions are key to enhancing learning performance and sample efficiency, thereby balancing exploration and exploitation more effectively. As part of our analysis, we offer a novel interpretation of Tolman's maze experiments, emphasizing the importance of free exploratory learning in the initial stages. Furthermore, using our Cross-Density Visualizer. we discover that S2D reward transitions smooth the policy loss landscape, promoting wide minima, which significantly enhances generalization.

## Videos

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
    <div style="margin: 10px;">
        <video width="200" autoplay loop>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-sparse.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    <div style="margin: 10px;">
        <video width="200" autoplay loop>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-dense-1.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    <div style="margin: 10px;">
        <video width="200" autoplay loop>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-s2d-1.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    <div style="margin: 10px;">
        <video width="200" autoplay loop>
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-d2s.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
</div>

## Key findings
- Transitioning from sparse-to-dense reward significantly improves learning outcomes, balancing exploration and exploitation to enhance success rates and sample efficiency.

- The S2D reward transition smooths the policy loss landscape, promoting wider minima and enhancing generalization.

- Agents' free exploration during the sparse reward phase forms good initial policy parameters, leading to more stable and faster learning when transitioning to dense rewards.

- We developed custom 3D environments for egocentric scenarios, including ViZDoom and the minecraft mazes, specialized for generalization measures.

