import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# Bubble sort with detailed steps for visualization
def bubble_sort_with_steps(arr):
    steps = []
    n = len(arr)
    step_num = 1
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append({
                "array": arr.copy(),
                "compare": (j, j+1),
                "pass": i + 1,
                "step": step_num,
                "swapped": False
            })
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append({
                    "array": arr.copy(),
                    "compare": (j, j+1),
                    "pass": i + 1,
                    "step": step_num,
                    "swapped": True
                })
            step_num += 1
    return steps

# Streamlit UI
st.title("🔁 Bubble Sort Visualization (Detailed)")
st.markdown("""
This app shows how **Bubble Sort** works, including:
- Current pass and step number
- Elements being compared
- Whether a swap occurred
""")

# Controls
size = st.slider("🔢 Select number of elements", min_value=5, max_value=30, value=10)
delay = st.slider("⏱ Delay between steps (seconds)", 0.01, 1.0, 0.3)

if st.button("▶️ Start Sorting"):
    arr = random.sample(range(1, 100), size)
    steps = bubble_sort_with_steps(arr.copy())

    chart = st.empty()
    initial_array = st.empty()
    status = st.empty()
    array_display = st.empty()

    # Display initial array before sorting starts
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color='skyblue')
    ax.set_title("Initial Unsorted Array")
    chart.pyplot(fig)
    initial_array.markdown(f"**Initial Array:** `{arr}`")
    time.sleep(delay)

    # Animate steps
    for step in steps:
        fig, ax = plt.subplots()
        bar_colors = ['green' if i in step["compare"] else 'skyblue' for i in range(len(step["array"]))]
        ax.bar(range(len(step["array"])), step["array"], color=bar_colors)
        ax.set_title(f"Pass {step['pass']} - Step {step['step']}")
        chart.pyplot(fig)

        # Update info
        i, j = step["compare"]
        array_display.markdown(f"**Current Array:** `{step['array']}`")
        action = "🔄 Swapped" if step["swapped"] else "🤝 Compared"
        status.markdown(f"**Pass {step['pass']}, Step {step['step']}**: Comparing `arr[{i}] = {step['array'][i]}` and `arr[{j}] = {step['array'][j]}` → {action}")

        time.sleep(delay)

    st.success("✅ Sorting Complete!")
