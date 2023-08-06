import sys, os 
import sys
#sys.path.append("../omniplot")
from omniplot  import plot as op
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
#test="dotplot"
#test="triangle_heatmap"
test="decomp"
test="manifold"
test="triangle_heatmap"
test="radialtree"
test="violinplot"
test="cluster"
test="regression"
test="dotplot"
test="regression"
test="nice_piechart_num"
test="pie_scatter"
test="correlation"
test="manifold"
test="stacked"
test="stackedlines"
test="correlation"
test="cluster"
test="radialtree"
test="scatterplot"
test="stacked_num"
test="complex_clustermap"
test="volcanoplot"
test="nice_piechart"
test="lines"

if test=="lines":
    f="/home/koh/data/omniplot/energy/owid-energy-data.csv"
    df=pd.read_csv(f)
    _df=df.loc[df["country"]=="Japan"]
    cols=['biofuel_consumption',
            'coal_consumption',
            'gas_consumption',
            'hydro_consumption',
            'nuclear_consumption',
            'oil_consumption',
            'other_renewable_consumption',
            'solar_consumption',
            'wind_consumption']
    op.lineplot(df=_df, x="year",y=cols,title="Japan", yunit="twh", split=True)
    plt.show()
elif test=="stackedlines":
    f="/home/koh/data/omniplot/energy/owid-energy-data.csv"
    df=pd.read_csv(f)
    _df=df.loc[df["country"]=="Japan"]
    cols=['biofuel_consumption',
            'coal_consumption',
            'gas_consumption',
            'hydro_consumption',
            'nuclear_consumption',
            'oil_consumption',
            'other_renewable_consumption',
            'solar_consumption',
            'wind_consumption']
    op.stackedlines(df=_df, x="year",y=cols,title="Japan", remove_all_zero=True, inverse=True,show_values=True, hatch=True, yunit="twh")
    
    _df=pd.DataFrame({"x":np.arange(100),
                        "y0":np.random.normal(loc=0.0, scale=1.0, size=100)-3,
                        "y1":np.random.normal(loc=0.0, scale=1.0, size=100)+3,
                        "y2":np.random.normal(loc=0.0, scale=1.0, size=100)-4})
    op.stackedlines(df=_df, x="x",y=["y0","y1", "y2"],title="Japan",bbox_to_anchor=[1,1], sort=True, remove_all_zero=False, inverse=False,show_values=False, yunit="twh")
    
    plt.show()
elif test=="nice_piechart":
    df=sns.load_dataset("penguins")
    df=df.dropna(axis=0)
    tmp=[]
    for num, (sp, i ,se) in enumerate(zip(df["species"], df["island"],df["sex"])):
        if num/df.shape[0] > 0.98:
            tmp.append("NA")
        else:
            tmp.append(sp[0]+"_"+i[0]+"_"+se[0])
    df["combine"]=tmp
    print(df)
    op.nice_piechart(df, category=["species", "island","sex"], order="",ncols=2,show_values=True,show_legend=True)
    plt.show()
elif test=="nested_piechart":
    # df=sns.load_dataset("titanic")
    # df=df[["class","embark_town","sex"]].fillna("NA")
    # op.nested_piechart(df, category=["class","embark_town","sex"], title="Titanic", 
    #                    ignore=0.01, 
    #                    show_legend=True,
    #                    show_values=False,
    #                    hatch=False, skip_na=True)
    df=sns.load_dataset("penguins")
    df[["species","sex","island"]]=df[["species","sex","island"]].fillna("NA")
    op.nested_piechart(df,
                       category=["species","sex","island"],
                       #variable="body_mass_g",
                       title="Penguins", 
                       ignore=0.01, 
                       show_legend=True,
                       show_values=False,
                       show_percentage=False,order="largest",
                       hatch=False, skip_na=True,colormode="independent")
    df=pd.read_csv("/home/koh/data/omniplot/energy/owid-energy-data_curated_with_continents.csv")
    df=df.loc[df["year"]==2021]
    op.nested_piechart(df,
                       category=["Continent","country"],
                       variable="coal_electricity",
                       title="Coal electricity in 2021 (terawatt-hours)", 
                       ignore=0.03, 
                       show_legend=True,
                       show_values=True,
                       show_percentage=True,order="largest",
                       hatch=False, skip_na=True,colormode="hierarchical")
    plt.show()
elif test=="stacked": 
    # df=sns.load_dataset("penguins")
    # df=df.dropna(axis=0)
    # op.stacked_barplot(df, x=["species","island"],
    #                     hue=["sex","island"], scale="absolute", order=[
    #                                                                 ["Chinstrap","Gentoo","Adelie"],
    #                                                                 ["Dream","Biscoe","Torgersen"]],
    #                     test_pairs=[["Adelie","Gentoo"]], hatch=True)
    # op.stacked_barplot(df, x="species",
    #                     hue="sex", scale="percentage", hatch=True)

    df=sns.load_dataset("titanic")
    op.stacked_barplot(df=df,x=["sex"],
                       hue=["age","alone"], 
                       bin_num=10, 
                       test_pairs=[["male", "female"]],
                       orientation="vertical",
                       scale="absolute")

    plt.show()
elif test=="stacked_num": 
    """          　Bournemouth    Brighton
        Possession         36          64
        Shots              14          16
        Shots on Target     3           6
        Corners             5           5
        Fouls              11           5
    """
    # fig, ax=plt.subplots()
    # df=pd.DataFrame({"Bournemouth":[36,14,3,5,11],
    # "Brighton":[64,16,6,5,5]}, 
    # index=["Possession","Shots","Shots on Target","Corners","Fouls"])
    # op.stacked_barplot_num(df=df,
    # show_values_intact=True, 
    #                        unit={"Possession":"%"}, 
    #                        horizontal=True,
    # ax=ax)
    
    mat=np.concatenate([0.25*np.random.uniform(0,1,size=[10, 25]),0.5*np.random.uniform(0,1,size=[15, 25]),
    np.random.uniform(0,1,size=[15, 25])])
    mat=np.concatenate([mat, np.random.uniform(0,1,size=[40, 15])], axis=1)
    _df=pd.DataFrame({"less":np.sum(mat<0.5, axis=1),"more":np.sum(mat>=0.5, axis=1)})
    op.stacked_barplot_num(df=_df,orientation="horizontal")
    # df=pd.read_csv("/media/koh/grasnas/home/data/omniplot/energy/owid-energy-data_curated_with_continents.csv")
    # df=df.loc[df["year"]==2021]
    # cols=["country","coal_consumption","gas_consumption","hydro_consumption","oil_consumption",
    #       "nuclear_consumption","biofuel_consumption","solar_consumption","wind_consumption"]
    # df=df[cols]
    # df=df.reindex()
    
    # srt=np.argsort(np.array(df.sum(axis=1)))[::-1]
    # df=df.iloc[srt[:10]]
    # print(df)
    # op.stacked_barplot_num(df=df,x="country",show_values=False,# show_values_intact=True, 
    #                        #unit={"Possession":"%"}, 
    #                        horizontal=True,scale="absolute",xlabel="kwh",legend_row_num=4)
    plt.show()

elif test=="nice_piechart_num":
    f="/home/koh/data/omniplot/energy_vs_gdp.csv"
    df=pd.read_csv(f, comment='#')
    df=df.set_index("country")
    op.nice_piechart_num(df, variables=['biofuel_electricity',
                                                    'coal_electricity',
                                                    'gas_electricity',
                                                    'hydro_electricity',
                                                    'nuclear_electricity',
                                                    'oil_electricity',
                                                    'other_renewable_electricity',
                                                    'solar_electricity',
                                                    'wind_electricity'],ncols=10)
    
    
    plt.show()
elif test=="correlation":
    df=sns.load_dataset("penguins")
    df=df.dropna(axis=0)
    
        
    op.correlation(df, category=["species", "island","sex"], method="pearson", ztransform=True)
    plt.show()

elif test=="regression":
    df=sns.load_dataset("penguins")
    df=df.dropna(axis=0)
    op.regression_single(df, x="bill_length_mm",y="body_mass_g", method="ransac",category="species")
    plt.show()
elif test=="dotplot":
    df=pd.DataFrame({"Experiments":["exp1","exp1","exp1","exp1","exp2","exp2","exp3"],
                        "GO":["nucleus","cytoplasm","chromosome","DNA binding","chromosome","RNA binding","RNA binding"],
                        "FDR":[10,1,5,3,1,2,0.5],
                        "odds":[3.3,1.1,2.5,2.1,0.8,2.3,0.9]})
    op.dotplot(df, row="GO",col="Experiments", size_val="FDR",color_val="odds", highlight="FDR",
    color_title="Odds", size_title="-log10 p",scaling=20)
    # df=pd.read_csv("/home/koh/ews/idr_revision/clustering_analysis/cellloc_longform.csv")
    # print(df.columns)
    # df=df.fillna(0)
    # #dotplot(df, size_val="pval",color_val="odds", highlight="FDR",color_title="Odds ratio", size_title="-log10 p value",scaling=20)
    #
    # dotplot(df, row="Condensate",col="Cluster", size_val="pval",color_val="odds", highlight="FDR",
    #         color_title="Odds", size_title="-log10 p value",scaling=20)
    plt.show()

elif test=="radialtree":
    df=sns.load_dataset("penguins")
    df=df.dropna(axis=0)
    variables=["bill_length_mm","bill_depth_mm","flipper_length_mm"]
    op.radialtree(df, variables=variables, category=["species","island","sex"])#,figsize=[8,8])
    plt.show()

elif test=="violinplot":
    df=sns.load_dataset("penguins")
    df=df.dropna(axis=0)
    op.violinplot(df,x="species",y="bill_length_mm", 
                pairs=[["Adelie","Chinstrap" ],["Gentoo","Chinstrap" ],["Adelie","Gentoo" ]],
                test="mannwhitneyu",
                significance="symbol",swarm=True)
    plt.show()

elif test=="violinplot2":
    df=sns.load_dataset("penguins")
    df=df.dropna(axis=0)
    op.violinplot2(df,x="species",y="bill_length_mm",
                   pairs=[["Adelie","Chinstrap" ],["Gentoo","Chinstrap" ],["Adelie","Gentoo" ]],
                swarm=True, orientation="vertical",scale_prop=True)
    plt.show()



elif test=="volcanoplot":
    df=pd.read_csv("/home/koh/vscode/omniplot/data/volcano.csv")
    res=op.volcanoplot(df=df, x="log2FC", y="p-value", label="GeneNames", rankby="both", topn_labels_right=3, xthreshold=2)
    print(res)
    plt.show()