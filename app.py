import gradio as gr
import random 

# this is the main function, the quick sort algothim. 
def quickSort(arr):

    try:
        arr = [int(x.strip()) for x in arr.split(",")]
    except:
        return "Error:"
    #This list is used to store the steps taken for the quick sort 
    swaps = []
    
    def quicksort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]

        # Records the steps into the swaps list 
        swaps.append(f"Pivot {pivot}: left={left}, right={right}")
        
        return quicksort(left) + [pivot] + quicksort(right)

    sortAry = quicksort(arr)
    sorted_text = ", ".join(map(str, sortAry))
    # Returns the quick sorted array and the steps taken to get there 
    return f"Sorted: {sorted_text}\n\nSteps:\n" + "\n".join(swaps)

# This function generates the random array 
def generate(size):
    arr = [random.randint(0, 100) for _ in range(size)]
    return ", ".join(map(str, arr))  

# This is the gradio UI section 
with gr.Blocks(title="Quick Sort Visualizer") as demo:

    gr.Markdown(" Quick Sort Visualizer\nGenerate a random array or enter your own")
    # the slider for the random array 
    with gr.Row():
        size_slider = gr.Slider(3, 20, value=8, step=1, label="Array Size")
        generate_btn = gr.Button("Generate Random Array")
    
    input_box = gr.Textbox(label="Array", placeholder="Array appears here")
    # The button for the quick sort 
    sort_btn = gr.Button("Sort Array")
    output_box = gr.Textbox(label="Sorted Array + Steps", lines=10)
    # event handlers 
    generate_btn.click(fn=generate, inputs=size_slider, outputs=input_box)
    sort_btn.click(fn=quickSort, inputs=input_box, outputs=output_box)

demo.launch()
