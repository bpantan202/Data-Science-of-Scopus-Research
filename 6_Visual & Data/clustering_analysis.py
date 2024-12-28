import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit Title
st.title("Clustering Analysis")

# File Upload
with open('cu_with_cluster.json', 'r') as file:
    data1 = json.load(file)

with open('ku_with_cluster.json', 'r') as file:
    data2 = json.load(file)

# Convert JSON to DataFrame
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Global Clustering Analysis
st.subheader("Global Clustering Analysis : Total Citations by Internationality")

# Create columns for side-by-side plots
col1, col2 = st.columns(2)

# Boxplot: Internationality vs Total Citations
with col1:
    st.subheader("Chulalongkorn University -- (CU)\nBoxplot:")
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df1, x="global_cluster", y="Num", palette="viridis")
    plt.title("Boxplot of Total Citations by Internationality")
    plt.xlabel("Internationality Cluster (0: Low, 1: High)")
    plt.ylabel("Total Citations")
    st.pyplot(plt.gcf())

    st.subheader(".\nDensity plot:")
    plt.figure(figsize=(6, 4))
    for cluster in df1["global_cluster"].unique():
        sns.kdeplot(df1[df1["global_cluster"] == cluster]["Num"], label=f"{"High Internationality"if cluster == "1" else "Low Internationality"} Cluster", shade=True)
    plt.title("Density Plot of Total Citations by Internationality Cluster")
    plt.xlabel("Total Citations")
    plt.ylabel("Density")
    plt.legend()
    st.pyplot(plt.gcf())

# Density Plot: Total Citations by Internationality Cluster
with col2:
    st.subheader("Kasetsart University -- (KU)\nBoxplot:")
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df2, x="global_cluster", y="Num", palette="viridis")
    plt.title("Boxplot of Total Citations by Internationality")
    plt.xlabel("Internationality Cluster (0: High, 1: Low)")
    plt.ylabel("Total Citations")
    st.pyplot(plt.gcf())

    st.subheader(".\nDensity plot:")
    plt.figure(figsize=(6, 4))
    for cluster in df2["global_cluster"].unique():
        sns.kdeplot(df2[df2["global_cluster"] == cluster]["Num"], label=f"{"High Internationality"if cluster == 0 else "Low Internationality"} Cluster", shade=True)
    plt.title("Density Plot of Total Citations by Global Cluster")
    plt.xlabel("Total Citations")
    plt.ylabel("Density")
    plt.legend()
    st.pyplot(plt.gcf())
    

# Newness Clustering Analysis
st.subheader("Newness Clustering Analysis : Total Citations by Newness")

# Create columns for side-by-side plots
col3, col4 = st.columns(2)
colors = {"0": "orange", "1": "blue"}

# Boxplot: Newness Cluster vs Total Citations
with col3:
    st.subheader("Chulalongkorn University -- (CU)\nBoxplot:")
    sns.boxplot(
        data=df1, 
        x="newness_cluster", 
        y="Num", 
        palette="viridis", 
        order=sorted(df1['newness_cluster'].unique(), reverse=False)
    )

    plt.title("Boxplot of Total Citations by Newness Cluster")
    plt.xlabel("Newness Cluster (0: High, 1: Low)")
    plt.ylabel("Total Citations")
    plt.legend([], [], frameon=False)
    st.pyplot(plt.gcf())

    st.subheader(".\nDensity plot:")
    plt.figure(figsize=(6, 4))
    for cluster in df1["newness_cluster"].unique():
        sns.kdeplot(df1[df1["newness_cluster"] == cluster]["Num"], label=f"{"High" if cluster == "0" else "Low"} Newness Cluster", shade=True, color=colors[str(cluster)])
    plt.title("Density Plot of Total Citations by Newness Cluster")
    plt.xlabel("Total Citations")
    plt.ylabel("Density")
    plt.legend()
    st.pyplot(plt.gcf())


# Density Plot: Total Citations by Newness Cluster
with col4:
    st.subheader("Kasetsart University -- (KU)\nBoxplot:")
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df2, x="newness_cluster", y="Num", palette="viridis")
    plt.title("Boxplot of Total Citations by Newness Cluster")
    plt.xlabel("Newness Cluster (0: High, 1: Low)")
    plt.ylabel("Total Citations")
    st.pyplot(plt.gcf())

    st.subheader(".\nDensity plot:")
    plt.figure(figsize=(6, 4))
    for cluster in df2["newness_cluster"].unique():
        sns.kdeplot(df2[df2["newness_cluster"] == cluster]["Num"], label=f"{"High" if cluster == 0 else "Low"} Newness Cluster", shade=True,  color=colors[str(cluster)])
    plt.title("Density Plot of Total Citations by Newness Cluster")
    plt.xlabel("Total Citations")
    plt.ylabel("Density")
    plt.legend()
    st.pyplot(plt.gcf())
