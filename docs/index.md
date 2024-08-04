# Toddler 👶 inspired reward transition

## Abstract

Consider the journey of toddlers: they progress from free exploration with sparse feedback to goal-directed learning with denser rewards. Inspired by this phenomenon, we aim to explore the \textbf{Toddler-Inspired Reward Transition} in goal-oriented reinforcement learning (RL) tasks. Our primary focus is on \textit{transitioning from sparse to potential-based dense (S2D) rewards} while maintaining optimal strategies. Through a series of experiments, including dynamic robotic arm manipulation tasks and egocentric 3D navigation tasks, our results show that proper S2D reward transitions are key to enhancing learning performance and sample efficiency, thereby balancing exploration and exploitation more effectively. As part of our analysis, we offer a novel interpretation of Tolman's maze experiments, emphasizing the importance of free exploratory learning in the initial stages. Furthermore, using our Cross-Density Visualizer. we discover that S2D reward transitions smooth the policy loss landscape, promoting wide minima, which significantly enhances generalization.

## Videos

<div align="center">
    <video width="600" controls>
        <source src="{{ site.baseurl }}/docs/assets/videos/s2d.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>