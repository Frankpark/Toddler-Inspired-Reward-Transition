# Toddler 👶 inspired reward transition

## Abstract

Consider the journey of toddlers: they progress from free exploration with sparse feedback to goal-directed learning with denser rewards. Inspired by this phenomenon, we aim to explore the \textbf{Toddler-Inspired Reward Transition} in goal-oriented reinforcement learning (RL) tasks. Our primary focus is on \textit{transitioning from sparse to potential-based dense (S2D) rewards} while maintaining optimal strategies. Through a series of experiments, including dynamic robotic arm manipulation tasks and egocentric 3D navigation tasks, our results show that proper S2D reward transitions are key to enhancing learning performance and sample efficiency, thereby balancing exploration and exploitation more effectively. As part of our analysis, we offer a novel interpretation of Tolman's maze experiments, emphasizing the importance of free exploratory learning in the initial stages. Furthermore, using our Cross-Density Visualizer. we discover that S2D reward transitions smooth the policy loss landscape, promoting wide minima, which significantly enhances generalization.

## Videos

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
            <source src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/videos/room-s2d-1.mp4" type="video/mp4">
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


## Key findings
- Transitioning from sparse-to-dense reward significantly improves learning outcomes, balancing exploration and exploitation to enhance success rates and sample efficiency.

- The S2D reward transition smooths the policy loss landscape, promoting wider minima and enhancing generalization.

- Agents' free exploration during the sparse reward phase forms good initial policy parameters, leading to more stable and faster learning when transitioning to dense rewards.

- We developed custom 3D environments for egocentric scenarios, including ViZDoom and the minecraft mazes, specialized for generalization measures.

<figure style="text-align: center; margin: 20px;">
    <img src="https://github.com/Frankpark/Toddler-Inspired-Reward-Transition/raw/main/docs/assets/images/toddleranalogy.png" alt="Toddler Analogy">
    <figcaption>This figure shows the analogy of agents' trajectories to toddlers' learning. (a) Learning trajectory of a toddler. On the left, a toddler's free exploration of an environment represents learning with sparse rewards. On the right, the toddler grows up, she tends to direct their journey towards specific objects, which signify goal-directed learning. Similarly, the agent's journey from sparse rewards to potential-based dense rewards is depicted by the arrow above, drawing a parallel between the learning processes of toddlers and agents.

(b) Summary of baseline rewards. Sparse rewards are only given when agents reach a target. In contrast, potential-based dense rewards are provided based on the agent's proximity to a target object, mimicking the reward transition observed in toddler learning.</figcaption>
</figure>



