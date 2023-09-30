import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# To load the data
@st.cache(allow_output_mutation=True)
def load_dataset():
    return pd.read_excel('modified_data.xlsx')

data = load_dataset()

# Here we are returning the 1-3-5 year returns
# Inside the year_returns() function
def year_returns():
    skew_labels=["Positively Skewed", "Positively Skewed", "Negatively Skewed"]
    fig, ax = plt.subplots(3, 1, figsize=(8, 16)) 

    sns.distplot(data['returns_1yr'], ax=ax[0], color='green') 
    ax[0].text(10.0, .12, skew_labels[0], fontsize=12)

    sns.distplot(data['returns_3yr'], ax=ax[1], color='purple')
    ax[1].text(10.0, .05, skew_labels[0], fontsize=12)

    sns.distplot(data['returns_5yr'], ax=ax[2], color='blue')
    ax[2].text(15.0, .150, skew_labels[2], fontsize=12)

    # Set x-axis tick labels and rotation
    # ax[2].set_xticks(range(len(data['returns_5yr'])))
    # ax[2].set_xticklabels(data['returns_5yr'], rotation='vertical')

    return fig


# Finding the categories
category = data['category'].unique().tolist()
category_freq = data['category'].value_counts().to_dict()

def getList(category_frequency):
    list = []
    for value in category_frequency.values():
        list.append(value)
    return list

category_count = getList(category_freq)

def scheme_categories():
    colors = ['deepskyblue', 'pink', 'green', 'red', 'yellowgreen']
    explode = (0.01, 0.01, 0.01, 0.01, 0.01)
    fig, ax = plt.subplots()
    ax.pie(category_count, explode=explode, labels=category, colors=colors, shadow=True, startangle=140, autopct='%1.1f%%')
    # ax.set_title('Scheme Categories', fontsize='24')
    ax.legend(category, loc='upper right', bbox_to_anchor=(1.50, 1.0), fontsize=15)
    ax.axis('equal')
    ax.set_aspect('equal')
    plt.rcParams['figure.figsize'] = (16, 10)
    plt.rcParams['font.size'] = 20
    return fig  # Return the Matplotlib figure not plt


# Rating frequency - 


rank=data['rating'].unique().tolist() #It returns list of items that are unique in the column "Crisil_Rating"
#print(rank)
rank_frequency = data['rating'].value_counts().to_dict() #It returns the count of each unique item in the form of dictionary
#print(rank_frequency)
count = rank_frequency.values() #It returns the "values" in key:value (unique item : frequency) pair of dictionary obtained in last line.
#print(count)

# function returns the list of rank_frequency
def getList(rank_frequency): 
    list = [] 
    for value in rank_frequency.values(): 
        list.append(value) 
          
    return list
      
rank_count=getList(rank_frequency) #This is to return list of values obtained in the dictionary.

#print(rank_count)
def rank_types():
    fig, ax = plt.subplots()
    labels = ['Rank 3', 'Rank 2', 'Rank 1', 'Rank 5', 'Rank 4']
    colors = ['green','deepskyblue','red', 'grey', 'pink']
    explode = (0.01, 0.01, 0.01, 0.01, 0.01)  

    # plot pie chart for crisil data
    ax.pie(rank_count, explode=explode, labels=labels, colors=colors, shadow=True, startangle=140, autopct='%1.1f%%')
    # ax.set_title('Rating', y=1.20, fontsize='24')
    ax.axis('equal')
    plt.rcParams['font.size'] = 12
    plt.rcParams['figure.figsize']=(16,6)
    ax.legend(labels,loc='upper right', bbox_to_anchor=(1.50,1.0), fontsize=15)
    
    return fig



# 1 Year Return
# X represents the fund scheme names
X = data['scheme_name'][:25]

def return_one_bar():
    

    # Assuming 'data' is defined and contains necessary data
    X = data['scheme_name'][:25]
    Y = data['returns_1yr'][:25]

    # Create a DataFrame for visualization
    df = pd.DataFrame({'Scheme Name': X, 'Returns (1 Years)': Y})

    # Highlight the bars with min and max returns
    min_return_idx = Y.idxmin()
    max_return_idx = Y.idxmax()

    # Plot the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(X, Y, color='deepskyblue', width=0.73)
    bars[min_return_idx].set_color('red')
    bars[max_return_idx].set_color('greenyellow')

    # Plot the line chart
    ax.plot(X, Y, linewidth=2.0, color='black', marker='o', markersize=6)

    ax.set_xlabel('Hybrid Mutual Funds', fontsize=24, fontname="Comic Sans MS")
    ax.set_ylabel('Returns in percentage', fontsize=24, fontname="Comic Sans MS")
    # ax.set_title('3 Year Returns(%)', y=1.20, fontsize=24)

    ax.set_xticks(X)
    ax.set_xticklabels(X, rotation='vertical')
    ax.grid()

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x(), yval + 0.15, f'{yval:.2f}', fontsize=10)
    
    return fig

def return_1yrs():
# Y represents the 1-year returns for the funds
    returns = data['returns_1yr'][:25]
    X = data['scheme_name'][:25]


    # Creating a line plot with annotations
    fig,ax = plt.subplots()
    ax.plot(X, returns, linewidth=3.0, color='deepskyblue', marker='o', markersize=10)

    # Adding labels and title
    ax.set_xlabel('Hybrid Mutual Funds', fontsize=24, fontname="Comic Sans MS")
    ax.set_ylabel('Returns in percentage', fontsize=24, fontname="Comic Sans MS" )
    # ax.set_title('1 Year Returns (%)', y=1.20, fontsize=24)

    # Adding legend and customizing
    labels = ['1 Year Return']
    ax.legend(labels, loc='upper right', fontsize=15)

    # Rotating x-axis labels and adding a grid
    ax.set_xticks(X, rotation='vertical')
    ax.set_xticklabels(X, rotation='vertical')
    ax.grid()

    for i, j in zip(X, returns):
        ax.annotate(str(j), xy=(i, j))

    # Setting figure size and font size
    plt.rcParams['figure.figsize'] = (20, 6)
    plt.rcParams['font.size'] = 14


    return fig

    # Displaying the plot
    # plt.show()
    


    # plt.show()

def return_three():
    

    # Assuming 'data' is defined and contains necessary data
    X = data['scheme_name'][:25]
    Y = data['returns_3yr'][:25]

    # Create a DataFrame for visualization
    df = pd.DataFrame({'Scheme Name': X, 'Returns (3 Years)': Y})

    # Highlight the bars with min and max returns
    min_return_idx = Y.idxmin()
    max_return_idx = Y.idxmax()

    # Plot the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(X, Y, color='grey', width=0.73)
    bars[min_return_idx].set_color('red')
    bars[max_return_idx].set_color('greenyellow')

    # Plot the line chart
    ax.plot(X, Y, linewidth=2.0, color='black', marker='o', markersize=6)

    ax.set_xlabel('Hybrid Mutual Funds', fontsize=24, fontname="Comic Sans MS")
    ax.set_ylabel('Returns in percentage', fontsize=24, fontname="Comic Sans MS")
    ax.set_title('3 Year Returns(%)', y=1.20, fontsize=24)

    ax.set_xticks(X)
    ax.set_xticklabels(X, rotation='vertical')
    ax.grid()

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x(), yval + 0.15, f'{yval:.2f}', fontsize=10)
    
    return fig

def return_3yrs_graph():
# Y represents the 1-year returns for the funds
    returns = data['returns_3yr'][:25]
    X = data['scheme_name'][:25]


    # Creating a line plot with annotations
    fig,ax = plt.subplots()
    ax.plot(X, returns, linewidth=3.0, color='deepskyblue', marker='o', markersize=10)

    # Adding labels and title
    ax.set_xlabel('Hybrid Mutual Funds', fontsize=24, fontname="Comic Sans MS")
    ax.set_ylabel('Returns in percentage', fontsize=24, fontname="Comic Sans MS" )
    # ax.set_title('1 Year Returns (%)', y=1.20, fontsize=24)

    # Adding legend and customizing
    labels = ['3 Year Return']
    ax.legend(labels, loc='upper right', fontsize=15)

    # Rotating x-axis labels and adding a grid
    ax.set_xticks(X, rotation='vertical')
    ax.set_xticklabels(X, rotation='vertical')
    ax.grid()

    for i, j in zip(X, returns):
        ax.annotate(str(j), xy=(i, j))

    # Setting figure size and font size
    plt.rcParams['figure.figsize'] = (20, 6)
    plt.rcParams['font.size'] = 14


    return fig


def return_five_bar():
    

    # Assuming 'data' is defined and contains necessary data
    X = data['scheme_name'][:25]
    Y = data['returns_5yr'][:25]

    # Create a DataFrame for visualization
    df = pd.DataFrame({'Scheme Name': X, 'Returns (5 Years)': Y})

    # Highlight the bars with min and max returns
    min_return_idx = Y.idxmin()
    max_return_idx = Y.idxmax()

    # Plot the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(X, Y, color='grey', width=0.73)
    bars[min_return_idx].set_color('red')
    bars[max_return_idx].set_color('greenyellow')

    # Plot the line chart
    ax.plot(X, Y, linewidth=2.0, color='black', marker='o', markersize=6)

    ax.set_xlabel('Hybrid Mutual Funds', fontsize=24, fontname="Comic Sans MS")
    ax.set_ylabel('Returns in percentage', fontsize=24, fontname="Comic Sans MS")
    ax.set_title('3 Year Returns(%)', y=1.20, fontsize=24)

    ax.set_xticks(X)
    ax.set_xticklabels(X, rotation='vertical')
    ax.grid()

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x(), yval + 0.15, f'{yval:.2f}', fontsize=10)
    
    return fig

def return_5yrs_graph():
# Y represents the 1-year returns for the funds
    returns = data['returns_5yr'][:25]
    X = data['scheme_name'][:25]


    # Creating a line plot with annotations
    fig,ax = plt.subplots()
    ax.plot(X, returns, linewidth=3.0, color='deepskyblue', marker='o', markersize=10)

    # Adding labels and title
    ax.set_xlabel('Hybrid Mutual Funds', fontsize=24, fontname="Comic Sans MS")
    ax.set_ylabel('Returns in percentage', fontsize=24, fontname="Comic Sans MS" )
    # ax.set_title('1 Year Returns (%)', y=1.20, fontsize=24)

    # Adding legend and customizing
    labels = ['5 Year Return']
    ax.legend(labels, loc='upper right', fontsize=15)

    # Rotating x-axis labels and adding a grid
    ax.set_xticks(X, rotation='vertical')
    ax.set_xticklabels(X, rotation='vertical')
    ax.grid()

    for i, j in zip(X, returns):
        ax.annotate(str(j), xy=(i, j))

    # Setting figure size and font size
    plt.rcParams['figure.figsize'] = (20, 16)
    plt.rcParams['font.size'] = 20


    return fig

def comparing():
    # Define bar width and labels
    barwidth = 0.25
    labels = ['1 Year Return', '3 Year Return', '5 Year Return']

    # Data extraction
    X = data['scheme_name'][:30]
    Y1 = data['returns_1yr'][:30]
    Y2 = data['returns_3yr'][:30]
    Y3 = data['returns_5yr'][:30]

    # Set position of bars and X axis
    r1 = np.arange(len(Y1))
    r2 = [x + barwidth for x in r1]
    r3 = [x + barwidth for x in r2]

    # Create the grouped bar chart
    fig, ax=plt.subplots()
    ax.bar(r1, Y1, color='green', width=barwidth, edgecolor='white', label='1 Year Return')
    ax.bar(r2, Y2, color='red', width=barwidth, edgecolor='white', label='3 Year Return')
    ax.bar(r3, Y3, color='deepskyblue', width=barwidth, edgecolor='white', label='5 Year Return')

    # Customize the plot add labels
    ax.set_xlabel('Hybrid Mutual Funds', fontsize = 24, fontname = 'Comic Sans MS')
    ax.set_ylabel('Returns in percentage', fontsize = 24, fontname = 'Comic Sans MS')
    ax.set_xticks(r1, X,  rotation ='vertical');
    plt.rcParams['figure.figsize'] = (20,6)
    plt.rcParams['font.size'] = 14
    ax.grid()
    ax.set_title('1 Year vs 3 Year vs 5 Year Returns(%)',y=1.20,fontsize=24,fontname="Comic Sans MS")
    ax.legend(labels, loc='upper right',bbox_to_anchor=(1.0,1.0),fontsize=15)
    
    return fig


def comparing_line():
    barwidth = 0.25
    labels = ['1 Year Return', '3 Year Return', '5 Year Return']
    X = data['scheme_name'][:30]
    Y1 = data['returns_1yr'][:30]
    Y2 = data['returns_3yr'][:30]
    Y3 = data['returns_5yr'][:30]

    # Set position of bars and X axis
    r1 = np.arange(len(Y1)) 
    r2 = [x + barwidth for x in r1]
    r3 = [x + barwidth for x in r2]
    fig,ax=plt.subplots()
    ax.plot(X, Y1, linewidth=3.0, color='red', marker='o', markersize=6, label='1 Year Return')
    ax.plot(X, Y2, linewidth=3.0, color='lime', marker='o', markersize=6, label='3 Year Return')
    ax.plot(X, Y3, linewidth=3.0, color='blue', marker='o', markersize=6, label='5 Year Return')

    # Customize the plot
    ax.set_xlabel('Hybrid Mutual Funds', fontsize=24, fontname="Comic Sans MS")
    ax.set_ylabel('Returns in percentage', fontsize=24, fontname="Comic Sans MS")
    ax.set_title('1 Year vs 3 Year vs 5 Year Returns(%)', y=1.20, fontsize=24)
    ax.legend(labels, loc='upper right', bbox_to_anchor=(1.0, 1.0), fontsize=15)
    ax.set_xticklabels(X, rotation='vertical')
    ax.grid()

    # Customize figure size and font size
    plt.rcParams['figure.figsize'] = (20, 6)
    plt.rcParams['font.size'] = 20

    # Display the plot
    plt.show()
    
# Calculate the indices for maximum and minimum returns for 1 year
most_return_1_year = data['returns_1yr'].idxmax()
less_return_1_year = data['returns_1yr'].idxmin()

# Retrieve the scheme names associated with the indices for 1 year
most_scheme_name_1yr = data.loc[most_return_1_year, 'scheme_name']
less_scheme_name_1yr = data.loc[less_return_1_year, 'scheme_name']

# Calculate the indices for maximum and minimum returns for 3 years
most_return_3_year = data['returns_3yr'].idxmax()
less_return_3_year = data['returns_3yr'].idxmin()

# Retrieve the scheme names associated with the indices for 3 years
most_scheme_name_3yr = data.loc[most_return_3_year, 'scheme_name']
less_scheme_name_3yr = data.loc[less_return_3_year, 'scheme_name']

# Calculate the indices for maximum and minimum returns for 5 years
most_return_5_year = data['returns_5yr'].idxmax()
less_return_5_year = data['returns_5yr'].idxmin()

# Retrieve the scheme names associated with the indices for 5 years
most_scheme_name_5yr = data.loc[most_return_5_year, 'scheme_name']
less_scheme_name_5yr = data.loc[less_return_5_year, 'scheme_name']




def distinguish():
    category_frequency = data['Good'].value_counts().to_dict()
    category_count = list(category_frequency.values())
    labels = ['Bad', 'Good']
    colors = ['red', 'lime']
    explode = (0.01, 0.01)

    fig, ax = plt.subplots()
    ax.pie(category_count, explode=explode, labels=labels, colors=colors, shadow=True, startangle=140, autopct='%1.1f%%')
    ax.legend(labels, loc='upper right', bbox_to_anchor=(1.5, 1.0), fontsize=15)
    ax.set_aspect('equal')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 20

    return fig







def main():
    st.title('Hybrid Mutual Fund Analysis')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Display the loaded data
    st.write('Displaying the dataset ')
    st.write(data)

    st.write('')
    st.write('')

    st.markdown(
        "<div style='border:1px solid black; padding:10px'>"
        "<h4 style> What is skew</h4>"
        "<p>Skewness is a measure of the asymmetry in the probability distribution of a set of numbers:</p>"
        "<ul><li>Positive skew: Leaning towards higher values (right side).</li>"
        "<li>Negative skew: Leaning towards lower values (left side)</li>"
        "<li>Zero skew: Balanced, no leaning</li></ul>"
        "<h2 style='text-align:center;'>Skewness</h2>"
        "</div>",
        unsafe_allow_html=True
    )

    year_returns_plot = year_returns()
    st.pyplot(year_returns_plot)
    st.write('')
    st.write('')

    st.markdown(
        "<div style='border:1px solid black; padding:10px'>"
        "<h2 style='text-align:center;'>Scheme Categories</h2>"    
        "<p><h2>Equity:</h2><ul><li>Ownership Stake: Equity represents ownership in a company or asset. When you own equity in a company, you have a stake in its ownership and potential profits.<li>"
        "<li>Risk and Reward: Investing in equity involves higher risk compared to other categories. The potential for high returns is also significant if the company performs well and its value increases.</li>"
        "<li>Long-Term Investment: Equity investments are typically considered long-term investments, aiming to benefit from the growth and success of the company over an extended period.</li>"
        "</ul>"
        "<h2>Hybrid:</h2>"

        "<ul></ul>"
        "<li>Blend of Assets: Hybrid funds combine different asset classes like equities, bonds, and sometimes other securities to provide investors with a diversified portfolio.</li>"
        "<li>Risk Management: The blend of assets allows for a balance between potential high returns (from equities) and stability (from bonds), managing overall risk.</li>"
        "<li>Flexibility: Hybrid funds offer flexibility for investors to adjust their portfolio based on market conditions, enabling them to align with their risk tolerance and financial goals.</li>"
        "<h2>Solution Oriented:</h2>"
        "<ul></ul>"
        "<li>Goal-Centric: These funds are designed to meet specific financial goals, such as retirement planning, child education, or buying a house, offering a structured approach to investment.</li>"
        "<li>Lock-In Period: Solution-oriented funds often have a lock-in period, ensuring that investors stay committed to achieving their financial objectives by discouraging premature withdrawals.</li>"
        "<li>Tax Benefits: In some regions, investments in solution-oriented funds may provide tax benefits, encouraging long-term savings towards targeted financial goals.</li>"
    "<h2>Other:</h2>"
    "<ul>"
        "<li><strong>Diverse Asset Classes:</strong> Wide range beyond equity, hybrid, and debt.</li>"
        "<li><strong>Tailored Strategies:</strong> Specialized approaches for unique objectives.</li>"
        "<li><strong>Varied Risk Levels:</strong> Risk varies based on asset or strategy.</li>"
    "</ul>"

    "<h2>Debt:</h2>"
    "<ul>"
        "<li><strong>Fixed Income:</strong> Involves bonds, government securities, providing regular interest.</li>"
        "<li><strong>Lower Risk:</strong> Generally lower risk, stable income.</li>"
        "<li><strong>Maturity and Principal Return:</strong> Has a maturity date, returns principal and interest.</li>"
    "</ul>"

        "</div>", unsafe_allow_html=True
    )
    scheme_categories_plot = scheme_categories()    
    st.pyplot(scheme_categories_plot)
    
    st.write(' ')
    st.write(' ')
    st.markdown(
        "<div style='border:1px solid black; padding:10px'>"
         "<h2 style='text-align:center;'>Rating</h2>"
        "<p> Rating is a method used to evaluate mutual funds and understand how well they are managed and performing. This evaluation is based on the best practices globally and considers various aspects of the mutual fund's portfolio and performance.</p>"

        "The evaluation involves analyzing a combination of Net Asset Value (NAV) and portfolio-based attributes. Here's what these terms mean:"
"<ul><li><b><h4>Net Asset Value (NAV):</b></h4> It's the value of each unit of the mutual fund. It's calculated by dividing the total value of all the securities in the portfolio by the total number of units issued to investors.</li>"
  
"<li><b><h4>Portfolio-based Attributes:</b></h4> These are characteristics of the mutual fund's investments, including asset allocation, asset concentration, liquidity (how easy it is to buy or sell), and the overall quality of the assets held by the fund.</li>"

"By considering these factors, rating offers a comprehensive analysis of mutual funds. The goal is to provide investors with a clear and simple understanding of how a particular mutual fund is likely to perform based on these critical parameters."

      
        "</div>"
        ,unsafe_allow_html=True
    )
    rank_types_plot = rank_types()
    st.pyplot(rank_types_plot)
    
    st.write('')
    st.write('')
    st.markdown("<div style='border:1px solid black; padding:10px'>"
         "<h2 style='text-align:center;'>1 Year Returns</h2>"
         "<p><b>As data is more than 750 so we are taking here only first 25</b></p>"
         "</div>",unsafe_allow_html=True)
    
    return_one_bar_plot = return_one_bar()
    st.pyplot(return_one_bar_plot)
    st.write('')
    return_1yrs_plot = return_1yrs()
    st.pyplot(return_1yrs_plot)


    st.markdown("<div style='border:1px solid black; padding:10px'>"
         "<h2 style='text-align:center;'>3 Year Returns</h2>"
         "<p><b>As data is more than 750 so we are taking here only first 25</b></p>"
         "</div>",unsafe_allow_html=True)

    return_three_plot = return_three()
    st.pyplot(return_three_plot)
    st.write('')
    return_3yrs_graph_plot = return_3yrs_graph()
    st.pyplot(return_3yrs_graph_plot)


    
    st.markdown("<div style='border:1px solid black; padding:10px'>"
         "<h2 style='text-align:center;'>5 Year Returns</h2>"
         "<p><b>As data is more than 750 so we are taking here only first 25</b></p>"
         "</div>",unsafe_allow_html=True)
    return_5yr_bar_plot=return_five_bar()
    st.pyplot(return_5yr_bar_plot)
    st.write('')
    return_5yrs_graph_plot=return_5yrs_graph()
    st.pyplot(return_5yrs_graph_plot)

    st.markdown("<div style='border:1px solid black; padding:10px'>"
         "<h2 style='text-align:center;'>1 year vs 3 year vs 5 year</h2>"
         "<p><b>As data is more than 750 so we are taking here only first 25</b></p>"
         "</div>",unsafe_allow_html=True)
    comparing_1_3_5_years = comparing()
    st.pyplot(comparing_1_3_5_years)
    
    st.write('')
    comparing_line_plot = comparing_line()
    st.pyplot(comparing_line_plot)

    st.write('')
    st.write('')

    st.markdown("<div><h2> 1st year return</h2></div>",unsafe_allow_html=True)
    st.write("Scheme with the most return in the past year:", most_scheme_name_1yr)
    st.write("Scheme with the least return in the past year:", less_scheme_name_1yr)
   
    st.markdown("<div><h2> 3rd year return</h2></div>",unsafe_allow_html=True)
    st.write("Scheme with the most return in the past 3 years:", most_scheme_name_3yr)
    st.write("Scheme with the least return in the past 3 years:", less_scheme_name_3yr)

    st.markdown("<div><h2> 5th year return</h2></div>",unsafe_allow_html=True)
    st.write("Scheme with the most return in the past 5 years:", most_scheme_name_5yr)
    st.write("Scheme with the least return in the past 5 years:", less_scheme_name_5yr)

    st.markdown("<div><h2> Good Schemes and Bad Schemes</h2><p><h5>Based on analysis on basis of parammeter we will distinguish between good and bad schemes</h5></div> ",unsafe_allow_html=True)
    distinguish_plot=distinguish()
    st.pyplot(distinguish_plot)

if __name__ == '__main__':
    main()
