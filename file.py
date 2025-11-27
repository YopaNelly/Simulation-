import streamlit as st
import pygame
import random
import matplotlib.pyplot as plt
from io import BytesIO

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("SIMNET II Bank Queue Simulation with Animation")

arrival_rate = st.slider("Customer Arrival Probability per Frame", 0.01, 0.2, 0.05, 0.01)
service_time_min = st.slider("Min Service Time (frames)", 10, 100, 20, 1)
service_time_max = st.slider("Max Service Time (frames)", 10, 100, 50, 1)
simulation_frames = st.slider("Number of Frames", 100, 1000, 300, 50)

if st.button("Run Simulation"):

    # -----------------------------
    # Initialize Pygame
    # -----------------------------
    pygame.init()
    WIDTH, HEIGHT = 800, 400
    screen = pygame.Surface((WIDTH, HEIGHT))  # use surface instead of window

    # -----------------------------
    # Customer Class
    # -----------------------------
    class Customer:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.served = False

        def draw(self, surface):
            color = (0, 200, 0) if self.served else (200, 0, 0)
            pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 10)

        def move_towards(self, target_y):
            if self.y < target_y:
                self.y += 2

    # -----------------------------
    # Simulation variables
    # -----------------------------
    queue = []
    queue_x = 150
    queue_start_y = 50
    queue_spacing = 40
    server_x = 600
    server_y = 200
    server_busy = False
    service_timer = 0
    customers_served = 0
    queue_lengths = []

    frames = []

    # -----------------------------
    # Simulation loop
    # -----------------------------
    for frame_num in range(simulation_frames):
        screen.fill((255, 255, 255))

        # Add new customer randomly
        if random.random() < arrival_rate:
            queue.append(Customer(queue_x, queue_start_y + len(queue)*queue_spacing))

        # Serve customer
        if not server_busy and queue:
            current = queue.pop(0)
            current.served = True
            server_busy = True
            service_timer = random.randint(service_time_min, service_time_max)

        if server_busy:
            service_timer -= 1
            pygame.draw.circle(screen, (0, 0, 255), (server_x, server_y), 20)  # server
            if service_timer <= 0:
                server_busy = False
                customers_served += 1

        # Move queue forward
        for i, c in enumerate(queue):
            target_y = queue_start_y + i*queue_spacing
            c.move_towards(target_y)
            c.draw(screen)

        # Draw queue length text
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render(f"Queue Length: {len(queue)}", True, (0, 0, 0))
        screen.blit(text_surface, (50, 10))

        # Save frame as image
        frame_str = pygame.image.tostring(screen, "RGB")
        frame_surf = pygame.image.fromstring(frame_str, (WIDTH, HEIGHT), "RGB")
        frames.append(frame_surf.copy())
        queue_lengths.append(len(queue))

    pygame.quit()

    # -----------------------------
    # Convert frames to images for Streamlit
    # -----------------------------
    st.subheader("Simulation Result — Queue Length Over Time")
    fig, ax = plt.subplots()
    ax.plot(queue_lengths, color='red')
    ax.set_xlabel("Frame")
    ax.set_ylabel("Queue Length")
    st.pyplot(fig)

    st.write(f"Total customers served: {customers_served}")
    st.write(f"Maximum queue length: {max(queue_lengths)}")

    # Optional: Show last frame as image
    last_frame = frames[-1]
    arr = pygame.surfarray.array3d(last_frame)
    arr = arr.transpose([1, 0, 2])
    st.image(arr, caption="Final Frame of Simulation")
