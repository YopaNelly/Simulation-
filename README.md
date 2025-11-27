# Simulation-

# **Bank Queue Simulation (SIMNET II) — Streamlit App**

## **Overview**

This project is a **bank queue simulation** inspired by the **SIMNET II discrete event simulation language**.

The app models a simple bank with:

* **Customers arriving randomly**
* **A single server (teller)** serving customers
* **A queue** where customers wait if the server is busy

The simulation includes:

* Animated **moving customers** (red circles for waiting, green if served)
* A **blue circle representing the server**
* **Queue length statistics** over time
* **Plots of queue length** and information about customers served

The app is built with:

* **Python**
* **Streamlit** (for interactive web interface)
* **Pygame** (for animation)
* **Matplotlib** (for plotting queue length over time)

---

## **Features**

* Real-time animation of customers moving through the bank queue
* Adjustable **customer arrival probability**
* Adjustable **service time** for the server
* Adjustable **number of frames** (simulation duration)
* Final **queue length plot**
* Displays **total customers served** and **maximum queue length**
* Shows **final frame** of the simulation

---

## **Requirements**

* Python 3.8+
* Streamlit
* Pygame
* Matplotlib

Install dependencies using:

```bash
pip install streamlit pygame matplotlib
```

---

## **How to Run**

1. Open a terminal / command prompt.
2. Navigate to the folder containing `bank_queue_app.py`.
3. Run the app:

```bash
streamlit run bank_queue_app.py
```

4. A browser window will open showing the **Streamlit app interface**.

---

## **How to Use**

1. **Adjust the sliders** to customize the simulation:

   * **Customer Arrival Probability per Frame:** Higher values generate more customers faster.
   * **Min/Max Service Time (frames):** Controls how long the server takes to serve each customer.
   * **Number of Frames:** Duration of the simulation (more frames = longer simulation).

2. Click **Run Simulation** to start:

   * Customers appear at the **queue start location** and move toward the server.
   * The **server is a blue circle**; when busy, it serves one customer at a time.
   * Customers turn **green** after being served.
   * **Queue length** updates dynamically.

3. After the simulation completes, the app displays:

   * **Queue length over time plot**
   * **Total customers served**
   * **Maximum queue length**
   * **Final frame** of the simulation (showing customer positions)

---

## **Screenshots**

<img width="759" height="515" alt="image" src="https://github.com/user-attachments/assets/89f30e94-305e-4072-96af-b21a625acde3" />


<img width="750" height="642" alt="image" src="https://github.com/user-attachments/assets/abd3d254-e050-4f6d-b6ca-0298dc6ae5b1" />


<img width="711" height="442" alt="image" src="https://github.com/user-attachments/assets/50f859c1-3edf-4544-bdd4-5068c8401346" />

---

## **Notes**

* This is a **local simulation**; it runs fully on your computer.
* You can **adjust parameters** to explore different scenarios (high traffic, slow server, etc.).
* Inspired by **SIMNET II nodes concept**: Source → Queue → Facility (Server) → Auxiliary (tracking stats).

---

✅ **Ready for Presentation**

* Works locally without internet
* Shows **animated customers** and real-time statistics
* Suitable for classroom demonstration

---
