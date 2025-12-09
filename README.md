title: CISC121Project
emoji: 🔥
colorFrom: red
colorTo: yellow
sdk: gradio
sdk_version: 6.0.2
app_file: app.py
pinned: false
---

The algorithm used: Quick Sort 

demo: The demo is in the Demo.pdf

Testing 
Normal cases 
Input 
4,1,6
Output 
1,4,6

Already sorted 
Input 
1,2,3
Output 
1,2,3

Errors
Input 
6,b,4
Output 
Error 

Decomposition - The website has a few main components, UI(user interface), input, the sorting algorithm itself, and then the output. The 
first thing the user will see is the user interface, like the website itself and the design. Then the user will input the array the user wants 
to be sorted. After that, the sorting algorithm, in this case quick sort, will sort the array. And the final step would be the output, the 
sorted array. 

Pattern Recognition - The quick sort works by repeating the same steps over and over again. Pick a pivot and then compare each number to the 
pivot, split the array, than recursively sort them. 

Abstraction - The main things to focus on would be the UI and sorting algorithm. The UI is what the user will see and interact with. And the 
sorting algorithm is the main component of the website. 

Algorithm Design - The process would go to user input(array ) then processing (quick sorting) and then output(the sorted array ). 

I chose to do quick sort because I like watching sorting algorithms work, it's nice to look at. Out of the sorting ones I chose Quick sort 
because I feel like it would look the coolest. I also believe that it’s the fastest one in practice, and therefore making it one of the best 
ones. 

Steps to run 
There is an array generator that can make an array for you and you can select the size of the array by moving the slider. You can also just 
enter the array you want to use by putting into the array text box. After that you can sort the array by pressing on the sort array button. 
After, the website will output the sorted array and the steps below it in the sorted + steps box. 

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

hugging face link: https://huggingface.co/spaces/billt876/CISC121Project 

Aurthor, Bill. I used chatGPT to help me make the UI using Gradio, I've never used Gradio before so it was a big help to me. I also asked 
chatGPT to help me add the steps at the end.
