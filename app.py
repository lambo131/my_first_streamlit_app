import streamlit as st
import pandas as pd
import numpy as np
import time

"""#This is my strealit playground"""


'''# magic input to display data'''
'''hi'''
st.write("hi")
a=3
'dataframe:', a
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df


'''# st.write()'''
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


'''# other display functions
    - st.write is auto rendered, use other funtions for customization
'''
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))
st.table(dataframe) # this is static


'''# Draw a line chart'''
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

'''# Plot a map'''
st.map(map_data)


"""# Widgets"""
'''slider'''
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
'''text input'''
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

text = st.text_input('text')
text


"""# checkboxs
    - checkboxs can be used show/hide data
"""
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


'''# select box
    - a list of selection
'''
df = pd.DataFrame({
    'options': [1, 2, 3, 4],
    })

option = st.selectbox(
    'Which number do you like best?',
     df['options'])

'You selected: ', option


'''# Layouts'''

'''sidebar - open sidebar on left upper corner to see'''
st.sidebar.write("This is the sidebar")
# Add a selectbox to the sidebar:
selection = add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
st.sidebar.write(f"your selection: {selection}")

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, 75.0
)
st.sidebar.write(f"value: {add_slider}")

'''columns - place widgets side by side'''
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!') 
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


'''# show progress'''
# Add a placeholder, no repeated text in loop
if st.button("run progress"):
    'Starting a long computation...'
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        # st.write(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)
    '...and now we\'re done!'


'''# Caching
    - cache expension function calls to improve performance
    - @st.cache_data is for caching serializable data(int, str, list, Dataframe)
    - @st.cache_resource is for caching unserializable data(tf.model)

'''
@st.cache_data
def expensive_func():
    summation = 0
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        # st.write(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)
        summation = summation+i
    latest_iteration.empty()
    bar.empty()
    return summation

leftbutton, rightbutton = st.columns(2)
if leftbutton.button("run expensive func"):
    start = time.time()
    st.write("output: ", expensive_func())
    end = time.time()
    st.write("time used: ", (end-start) * 10**3, "ms")
if rightbutton.button("clear cache"):
    st.cache_data.clear()


'''# pages
    - create multiple pages by creating new streamlit programs in "pages" folder in the same director as the main page program
'''
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

