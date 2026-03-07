import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from IPython.display import display, Markdown
import os
from scipy.stats import ks_2samp


class ResultsDataset():

    def check_for_group_consistency(self, ds, grouped_keywords, excluded_keywords):
        if not len(grouped_keywords.keys()) > 0:
            meta_cols = ["domain_name", "code", "ds", "kw_extractor"]
            keywords = [col for col in ds.columns if col not in meta_cols]
            keywords = [col for col in keywords if col not in excluded_keywords]
            # Every key is a group
            return {item: [item] for item in keywords}
        else:
            return grouped_keywords


    def load_results(self,language, keyword_extractor):

        sns.set(style="whitegrid")
        res = []
        results_f = os.path.join(os.path.dirname(os.getcwd()), 'results', language, keyword_extractor)
        csv = [file for file in os.listdir(results_f) if file.endswith('.csv')]
        for filename in csv:
            if not "parsing" in filename:
                res.append(pd.read_csv( os.path.join(results_f, filename) ))
        return res   

    def filter_and_group_keywords(self, df, excluded_keywords=None, grouped_keywords=None):
        excluded_keywords = excluded_keywords or []
        grouped_keywords = grouped_keywords or {}
        
        # Columns to always keep
        always_keep = ['domain_name', 'code', 'ds']
        
        # --- Step 1: Drop excluded columns (except the always_keep ones)
        cols_to_keep = [col for col in df.columns if col not in excluded_keywords or col in always_keep]
        df = df[cols_to_keep].copy()
        
        # --- Step 2: Handle grouping
        for group_name, members in grouped_keywords.items():
            # Keep only columns that actually exist
            valid_members = [m for m in members if m in df.columns]
            if valid_members:
                # Create new group column as the sum of the valid members
                df.loc[:, group_name] = df[valid_members].sum(axis=1)
                # Drop the individual member columns
                df = df.drop(columns=valid_members)
        
        return df

    def load_dataset_for_language(self, language):
        files = self.load_results(language.lower(),"regex")
        ds1 = pd.concat(files)
        ds1["kw_extractor"] = "Regex"

        files = self.load_results(language.lower(),"lexer")
        ds2 = pd.concat(files)
        ds2["kw_extractor"] = "Lexer"

        files = self.load_results(language.lower(),"parser")
        ds3 = pd.concat(files)
        ds3["kw_extractor"] = "Parser"

        return pd.concat([ds1, ds2, ds3])
    
    def load_syntactic_analysis_dataset_for_language(self, language):
        syntactically_correct_kw = []
        total_kw = []
        rule_usage_vectors = []
        rule_correct_vectors = []
        rule_usage_accuracy = []
        rule_errors = []
        parser_lexer_errors = []
        tree_depth_and_size = []
        sequences = []

        results_f = os.path.join(os.path.dirname(os.getcwd()), 'results', language, 'SyntacticalAnalysis')
        csv = [file for file in os.listdir(results_f) if file.endswith('.csv')]
        for filename in csv:
            if "_syntactically_correct_kw" in filename:
                syntactically_correct_kw.append(pd.read_csv( os.path.join(results_f, filename) ))
            if "_total_kw" in filename:
                total_kw.append(pd.read_csv( os.path.join(results_f, filename) ))
            elif "_rule_usage_vectors" in filename:
                rule_usage_vectors.append(pd.read_csv( os.path.join(results_f, filename) ))
            elif "_rule_correct_vectors" in filename:
                rule_correct_vectors.append(pd.read_csv( os.path.join(results_f, filename) ))
            elif "_rule_usage_accuracy" in filename:
                rule_usage_accuracy.append(pd.read_csv( os.path.join(results_f, filename) ))
            elif "_rule_errors" in filename:
                rule_errors.append(pd.read_csv( os.path.join(results_f, filename) ))
            elif "_parser_lexer_errors" in filename:
                parser_lexer_errors.append(pd.read_csv( os.path.join(results_f, filename) ))
            elif "_tree_depth_and_size" in filename:
                tree_depth_and_size.append(pd.read_csv( os.path.join(results_f, filename) ))
            elif "_sequences" in filename:
                sequences.append(pd.read_csv( os.path.join(results_f, filename) ))

        return pd.concat(syntactically_correct_kw), pd.concat(total_kw), pd.concat(rule_usage_vectors), pd.concat(rule_correct_vectors), pd.concat(rule_usage_accuracy), pd.concat(rule_errors), pd.concat(parser_lexer_errors), pd.concat(tree_depth_and_size), pd.concat(sequences)

    def check_for_invalid_accuracy(self, total_frequencies, accuracy_df):
        # Check accuracy
        for ds in total_frequencies.keys():
            ser = accuracy_df.loc[ds]

            if ser is None:
                print(f"accuracy['{ds}'] not found")
            else:
                over = ser[ser > 1]
                if over.empty:
                    print(f"No Syntactic validity > 1 in '{ds}'")
                else:
                    df_over = over.sort_values(ascending=False).reset_index()
                    df_over.columns = ["Keyword", "Syntactic validity"]
                    print(f"Found {len(df_over)} items with Syntactic Validity > 1 in accuracy['{ds}']:")          


class ResultsGraph():

    def __init__(self, df):
        self.df = df 

    def keyword_coverage_per_dataset_by_extractor(self, datasets=[], append_to_title="", ds_labels=None, size=(10, 6), save_pdf=None):
        coverage_df = ResultsCoverage(self.df).compute_coverage_by_ds_extractor()  

        if len(datasets) > 0:
            coverage_df = coverage_df[coverage_df["ds"].isin(datasets)]      

        # Pivot for plotting (rows = ds, columns = kw_extractor)
        pivot_df = coverage_df.pivot(index="ds", columns="kw_extractor", values="coverage_pct")

        # Rename index if custom labels provided
        if ds_labels is not None:
            pivot_df = pivot_df.rename(index=ds_labels)

        # Define desired order, but keep only extractors that exist
        kw_order = ["Regex", "Lexer", "Parser"]
        existing_extractors = [kw for kw in kw_order if kw in pivot_df.columns]
        pivot_df = pivot_df[existing_extractors]

        # Plot grouped bar chart
        plt.figure(figsize=size)

        x = np.arange(len(pivot_df))
        bar_width = 0.8 / len(existing_extractors) if existing_extractors else 0.8

        for i, extractor in enumerate(existing_extractors):
            plt.bar(
                x + i * bar_width - (bar_width * len(existing_extractors) / 2),
                pivot_df[extractor],
                width=bar_width,
                label=extractor,
            )
        
        plt.ylim(0, 100)
        plt.title("Keyword Coverage" + append_to_title)
        plt.xticks(x, pivot_df.index)
        plt.xlabel("Dataset")
        plt.ylabel("Keyword Coverage (%)")
        plt.legend(title="Keyword Extractor")
        plt.tight_layout()

        if save_pdf is not None:
            plt.title("")
            plt.savefig(f"{save_pdf}.pdf")   

        plt.show()     
    
    def keyword_frequency(self, width=10, append_to_title=""):
        fig, ax = plt.subplots(figsize=(width, 6))
        self.df.plot(
            kind="bar",
            x="keyword",
            y="total_frequency",
            legend=False,
            ax=ax  # attach the plot to the figure's axes
        )
        ax.set_title(f"Keywords Frequency {append_to_title}")
        ax.set_xlabel("Keyword")
        ax.set_ylabel("Total Occurrences")
        plt.xticks(rotation=90)
        plt.show()

    def keyword_frequency_by_dataset_heatmap(self, size=20, filter_ds=None):
        data = self.df
        ds = data
        if not filter_ds is None:
            ds = data[data["ds"].isin(filter_ds)]
        ds = ResultsCoverage(ds).filter_kw_extractor_to_lexer()
        
        # Group by "ds" and sum all numeric columns
        grouped_sum = ds.groupby("ds").sum(numeric_only=True)

        # Normalize frequencies by "ds" (row-wise normalization)
        grouped_sum = grouped_sum.div(grouped_sum.sum(axis=1), axis=0)

        # Filter out columns where all values are 0 across all datasets
        grouped_sum = grouped_sum.loc[:, (grouped_sum != 0).any(axis=0)]

        # Transpose the DataFrame for the heatmap
        heatmap_data = grouped_sum.T

        # Plot the heatmap
        plt.figure(figsize=(8, size))
        sns.heatmap(heatmap_data, annot=False, fmt=".2f", cmap="Blues", cbar_kws={'label': 'Normalized Frequency'})
        plt.title("Normalized Keyword Frequency by Dataset (Lexer)")
        plt.gcf().autofmt_xdate()
        plt.xlabel("Dataset")
        plt.ylabel("Keyword")
        plt.tight_layout()
        plt.show()
    
    def syntactically_correct_rule_usage_distribution(self, rule_usage_accuracy_ds, filter=None):
        filtered_df = rule_usage_accuracy_ds
        if filter is not None:
            # Filter the dataset
            filtered_df = rule_usage_accuracy_ds[rule_usage_accuracy_ds['ds'].isin(filter)].copy()
            # Enforce the order of 'ds' based on the filter
            filtered_df['ds'] = pd.Categorical(filtered_df['ds'], categories=filter, ordered=True)
            # Sort by the categorical order
            filtered_df = filtered_df.sort_values('ds')

        # Create subplots for the violin plot and boxplot
        fig, axes = plt.subplots(1, 2, figsize=(11, 6), sharey=True)

        # Violin plot
        sns.violinplot(
            data=filtered_df,
            x='ds',
            y='accuracy',
            hue='ds',
            palette="muted",
            legend=False,
            inner="quartile",
            cut=0,
            ax=axes[0]
        )
        axes[0].set_title('Violin Plot: Syntactic Validity Distribution')
        axes[0].set_xlabel('Dataset')
        axes[0].set_ylabel('Syntactic Validity')
        axes[0].tick_params(axis='x', rotation=45)

        # Boxplot
        sns.boxplot(
            data=filtered_df,
            x='ds',
            y='accuracy',
            hue='ds',
            palette="muted",
            legend=False,
            ax=axes[1]
        )
        axes[1].set_title('Box Plot: Syntactic Validity Distribution')
        axes[1].set_xlabel('Dataset')
        axes[1].set_ylabel('Syntactic Validity')
        axes[1].tick_params(axis='x', rotation=45)

        # Adjust layout
        plt.tight_layout()
        plt.show()

    def plot_heatmap_rule_usage_summary(self, rules_usage_summary, ds_filter=None, top_n=None):
        # Filter the datasets based on the provided filter
        filtered_summary = rules_usage_summary
        if ds_filter is not None:
            filtered_summary = {key: rules_usage_summary[key] for key in ds_filter if key in rules_usage_summary}
        
        # Combine all filtered dataframes into one
        all_data = pd.concat(filtered_summary.values(), keys=filtered_summary.keys(), names=["Dataset"])
        all_data = all_data.reset_index(level="Dataset")  # Add the dataset name as a column
        
        # Ensure usage_ratio is 0 when usage_count is 0 (not NaN or small values)
        all_data['usage_ratio'] = np.where(all_data['usage_count'] == 0, 0, all_data['usage_ratio'])
        
        # Pivot tables for "usage_ratio" and "accuracy"
        usage_pivot = all_data.pivot(index="rule", columns="Dataset", values="usage_ratio").fillna(0)
        accuracy_pivot = all_data.pivot(index="rule", columns="Dataset", values="accuracy").fillna(0)
        
        # Optionally filter to top N rules by average usage ratio
        if top_n is not None:
            avg_usage = usage_pivot.mean(axis=1).sort_values(ascending=False)
            top_rules = avg_usage.head(top_n).index
            usage_pivot = usage_pivot.loc[top_rules]
            accuracy_pivot = accuracy_pivot.loc[top_rules]
        
        # Sort rules alphabetically
        usage_pivot = usage_pivot.sort_index()
        accuracy_pivot = accuracy_pivot.sort_index()
        
        # Plotting the heatmaps
        fig, axes = plt.subplots(2, 1, figsize=(12, max(8, len(usage_pivot) * 0.5)))
        
        # Heatmap for "usage_ratio"
        sns.heatmap(usage_pivot, annot=True, fmt=".2f", cmap="Blues", cbar_kws={'label': 'Usage Ratio'}, ax=axes[0])
        axes[0].set_title("Rule Usage Ratio across Datasets")
        axes[0].set_xlabel("Dataset")
        axes[0].set_ylabel("Rule")
        
        # Heatmap for "accuracy"
        sns.heatmap(accuracy_pivot, annot=True, fmt=".2f", cmap="Greens", cbar_kws={'label': 'Syntactic Validity'}, ax=axes[1])
        axes[1].set_title("Rule Syntactic Validity across Datasets")
        axes[1].set_xlabel("Dataset")
        axes[1].set_ylabel("Rule")
        
        # Adjust layout
        plt.tight_layout()
        plt.show()        
   

    def plot_avg_rule_usage_accuracy_by_dataset(self, rule_usage_avg_accuracy):
        # Sort the dataframe by avg_accuracy for better visualization
        rule_usage_avg_accuracy = rule_usage_avg_accuracy.sort_values(by="avg_accuracy", ascending=False)

        # Create the horizontal bar chart
        plt.figure(figsize=(10, 6))
        plt.barh(rule_usage_avg_accuracy["ds"], rule_usage_avg_accuracy["avg_accuracy"], color="skyblue")

        # Add labels and title
        plt.xlabel("Average Syntactic Validity")
        plt.ylabel("Dataset")
        plt.title("Average Rule Usage Syntactic Validity by Dataset")
        plt.gca().invert_yaxis()  # Invert y-axis to show the highest accuracy at the top
        plt.tight_layout()

        # Show the plot
        plt.show()
    
    def plot_rule_error_types_for_ds(self, ds, rule_errors_ds):
        if rule_errors_ds.empty or len(rule_errors_ds[rule_errors_ds["ds"] == ds]) == 0:
            display(Markdown("⚠️ **Warning:** No rule errors were found!"))
            return None

        subset = rule_errors_ds[rule_errors_ds["ds"] == ds].drop(columns=["error"], errors="ignore")

        grouped = (
            subset
            .groupby(["rule", "error_type"], observed=True)
            .size()
            .reset_index(name="count")
        )

        # compute percentage of errors per rule
        grouped["total_per_rule"] = grouped.groupby("rule", observed=True)["count"].transform("sum")
        grouped["percent"] = (grouped["count"] / grouped["total_per_rule"]).fillna(0)
        grouped = grouped.drop(columns=["total_per_rule"])

        # pivot for plotting: rules as rows, error_type as columns
        pivot = grouped.pivot_table(index="rule", columns="error_type", values="percent", fill_value=0)

        # sort rows (rules) by total error ratio
        rule_order = pivot.sum(axis=1).sort_values(ascending=False).index
        pivot = pivot.loc[rule_order]

        # plot heatmap
        plt.figure(figsize=(max(12, len(pivot.columns) * 0.5), max(6, len(pivot.index) * 0.4)))
        sns.heatmap(pivot, cmap="Reds", linewidths=.5, annot=True, fmt=".2f", cbar_kws={'label': 'Error Ratio'})
        plt.title(f"Error Group Composition (ratio) per Rule — {ds}")
        plt.xlabel("Error Group")
        plt.ylabel("Rule")
        plt.xticks(rotation=45, ha="right")
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.show()
    
    def plot_error_type_ratio_per_dataset(self, parser_lexer_errors, filter=None):
        if filter is None:
            filter = self.df["ds"].unique()
                
        target = pd.DataFrame()
        target = parser_lexer_errors[parser_lexer_errors["ds"].isin(filter)]
        if target.empty:
           display(Markdown("⚠️ **Warning:** No lexer or paser errors were found!"))
        else:
            error_counts = (
                target.groupby(['ds', 'error_type'])
                .size()
                .reset_index(name='count')
            )
            # compute percentage of errors within each dataset and replace 'count' with percent for plotting
            error_counts['percent'] = error_counts.groupby('ds')['count'].transform(lambda x: x / x.sum())
            error_counts = error_counts.drop(columns=['count'])

            plt.figure(figsize=(10,6))
            sns.barplot(
                data=error_counts,
                x='ds', y='percent', hue='error_type'
            )
            plt.title("ANTLR Error Type ratio per Dataset")
            plt.xlabel("Dataset")
            plt.ylabel("Ratio")
            plt.xticks(rotation=45, ha='right')
            plt.legend(title='Error Type')
            plt.tight_layout()
            plt.show()
    
    def plot_error_stage_per_dataset(self, parser_lexer_errors, filter=None):
        if filter is None:
            filter = self.df["ds"].unique()

        target = pd.DataFrame()
        target = parser_lexer_errors[parser_lexer_errors["ds"].isin(filter)]
        if target.empty:
           display(Markdown("⚠️ **Warning:** No lexer or paser errors were found!"))
        else:
            error_counts = (
                target.groupby(['ds', 'stage'])
                .size()
                .reset_index(name='count')
            )
            # compute percentage of errors within each dataset and replace 'count' with percent for plotting
            error_counts['percent'] = error_counts.groupby('ds')['count'].transform(lambda x: x / x.sum())
            error_counts = error_counts.drop(columns=['count'])

            plt.figure(figsize=(10,6))
            sns.barplot(
                data=error_counts,
                x='ds', y='percent', hue='stage'
            )
            plt.title("ANTLR Error Stages ratio per Dataset")
            plt.xlabel("Dataset")
            plt.ylabel("Ratio")
            plt.xticks(rotation=45, ha='right')
            plt.legend(title='Error stage')
            plt.tight_layout()
            plt.show()

    def plot_heatmap_keyword_usage(self, grouped_tables, ds_filter=None):
        # Filter the datasets based on the provided filter_ds list
        filtered_tables = grouped_tables
        if not ds_filter is None:
            filtered_tables = {key: grouped_tables[key] for key in ds_filter if key in grouped_tables}

        # Combine all filtered dataframes into one, ensuring all groups are included
        all_data = pd.concat(filtered_tables.values(), keys=filtered_tables.keys(), names=["Dataset"])
        all_data = all_data.reset_index(level="Dataset")  # Add the dataset name as a column

        # Pivot tables for "Uses" and "Correctly"
        uses_pivot = all_data.pivot(index="Group", columns="Dataset", values="Uses").fillna(0)
        correctly_pivot = all_data.pivot(index="Group", columns="Dataset", values="Correctly").fillna(0)

        # Plotting the heatmaps
        fig, axes = plt.subplots(2, 1, figsize=(12, 14))

        # Heatmap for "Uses"
        sns.heatmap(uses_pivot, annot=True, fmt=".2f", cmap="Blues", cbar_kws={'label': 'Group Coverage Ratio (GCR)'}, ax=axes[0], vmin=0, vmax=1)
        axes[0].set_title("Keyword used")
        axes[0].set_xlabel("")
        axes[0].set_ylabel("Keyword group")

        # Heatmap for "Correctly"
        sns.heatmap(correctly_pivot, annot=True, fmt=".2f", cmap="Greens", cbar_kws={'label': 'Group Parse Validity (GPV)'}, ax=axes[1], vmin=0, vmax=1)
        axes[1].set_title("Keyword used correctly")
        axes[1].set_xlabel("\nDataset")
        axes[1].set_ylabel("Keyword group")

        # Adjust layout
        plt.tight_layout()
        plt.show()    

    def plot_heatmap_keyword_usage_short(self, grouped_tables, ds_filter=None, keyword_filter=None, ds_labels=None, size=(10, 4), vspace=0.3, save_pdf=None):
        # Filter the datasets based on the provided filter_ds list
        filtered_tables = grouped_tables
        if not ds_filter is None:
            filtered_tables = {key: grouped_tables[key] for key in ds_filter if key in grouped_tables}

        # Combine all filtered dataframes into one, ensuring all groups are included
        all_data = pd.concat(filtered_tables.values(), keys=filtered_tables.keys(), names=["Dataset"])
        all_data = all_data.reset_index(level="Dataset")  # Add the dataset name as a column

        # Filter keywords/groups if specified
        if keyword_filter is not None:
            all_data = all_data[all_data["Group"].isin(keyword_filter)]

        # Pivot tables for "Uses" and "Correctly"
        uses_pivot = all_data.pivot(index="Group", columns="Dataset", values="Uses").fillna(0)
        correctly_pivot = all_data.pivot(index="Group", columns="Dataset", values="Correctly").fillna(0)

        # Rename columns if custom labels provided
        if ds_labels is not None:
            uses_pivot = uses_pivot.rename(columns=ds_labels)
            correctly_pivot = correctly_pivot.rename(columns=ds_labels)

        # Plotting the heatmaps
        fig, axes = plt.subplots(2, 1, figsize=size)

        # Heatmap for "Uses"
        sns.heatmap(uses_pivot, annot=True, fmt=".2f", cmap="Blues", cbar_kws={'label': 'Group Coverage Ratio (GCR)'}, ax=axes[0], vmin=0, vmax=1)
        axes[0].set_title("Keyword used")
        axes[0].set_xlabel("")
        axes[0].set_ylabel("Keyword group")

        # Heatmap for "Correctly"
        sns.heatmap(correctly_pivot, annot=True, fmt=".2f", cmap="Greens", cbar_kws={'label': 'Group Parse Validity (GPV)'}, ax=axes[1], vmin=0, vmax=1)
        axes[1].set_title("Keyword used correctly")
        axes[1].set_xlabel("\nDataset")
        axes[1].set_ylabel("Keyword group")


        for ax in axes:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

        # Adjust layout with custom vertical spacing
        plt.tight_layout()
        plt.subplots_adjust(hspace=vspace)
        
        if save_pdf is not None:
            plt.savefig(f"{save_pdf}.pdf")   

        plt.show()


    def plot_variance_analysis(self, datasets=None):
        df = self.df
        df[df["kw_extractor"]=="Lexer"]

        if datasets is None:
            datasets = df["ds"].unique()

        res = {}
        for ds in datasets:
            meta_cols = ["domain_name", "code", "ds", "kw_extractor"]
            keyword_cols = [col for col in df.columns if col not in meta_cols]
            ds_t = df[df["ds"]==ds][keyword_cols]
            res[ds] = np.var(ds_t, axis=0)

        df = pd.DataFrame({
            model: (vals if isinstance(vals, pd.Series) else pd.Series(vals, index=keyword_cols))
            for model, vals in res.items()
        })
        # Ensure rows follow rule_cols order
        df = df.reindex(keyword_cols)

        # Optional: sort rules by mean variance to make patterns clearer
        df = df.sort_values(by=list(df.columns), axis=0, ascending=False)

        # Plot heatmap
        plt.figure(figsize=(max(6, len(df.columns)*0.6), max(8, len(df.index)*0.18)))
        sns.heatmap(df, cmap="Blues", cbar_kws={"label": "variance"}, linewidths=0.3)
        plt.xlabel("Model")
        plt.ylabel("Keyword")
        plt.title("Variance of keyword usage per model")
        plt.xticks(rotation=45, ha="right")
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.show()        

    def plot_rule_variance_analysis(self, rule_usage_vectors_ds, datasets=None):
        res = {}

        if datasets is None:
            datasets = self.df["ds"].unique()

        for ds in datasets:
            ds_t = rule_usage_vectors_ds[rule_usage_vectors_ds["ds"]==ds].drop(columns=["ds"])
            res[ds] = np.var(ds_t, axis=0)

        rule_cols = rule_usage_vectors_ds.columns.drop("ds")

        df = pd.DataFrame({
            model: (vals if isinstance(vals, pd.Series) else pd.Series(vals, index=rule_cols))
            for model, vals in res.items()
        })

        # Ensure rows follow rule_cols order
        df = df.reindex(rule_cols)

        # Optional: sort rules by mean variance to make patterns clearer
        df = df.sort_values(by=list(df.columns), axis=0, ascending=False)

        # Plot heatmap
        plt.figure(figsize=(max(6, len(df.columns)*0.6), max(8, len(df.index)*0.18)))
        sns.heatmap(df, cmap="Blues", cbar_kws={"label": "variance"}, linewidths=0.3)
        plt.xlabel("Model")
        plt.ylabel("Rule")
        plt.title("Variance of rule usage per model")
        plt.xticks(rotation=45, ha="right")
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.show()
    

    def plot_tree_depth_and_size_analisis(self, df, group=None):

        if group is None:
            group = self.df["ds"].unique()

        df_sub = df.copy()
        if not group is None:
            df_sub = df[df['ds'].isin(group)].copy()
            # Enforce the order of 'ds' based on the group
            df_sub['ds'] = pd.Categorical(df_sub['ds'], categories=group, ordered=True)
            # Sort by the categorical order
            df_sub = df_sub.sort_values('ds')

        # Create subplots for tree depth: violin and box plots
        fig, axes = plt.subplots(1, 2, figsize=(11, 6), sharey=True)

        # Violin plot for tree depth
        sns.violinplot(
            data=df_sub,
            x='ds',
            y='tree_depth',
            hue='ds',
            palette="muted",
            legend=False,
            inner="quartile",
            cut=0,
            ax=axes[0]
        )
        axes[0].set_title('Violin Plot: Tree Depth Distribution')
        axes[0].set_xlabel('Dataset')
        axes[0].set_ylabel('Tree Depth')
        axes[0].tick_params(axis='x', rotation=45)

        # Boxplot for tree depth
        sns.boxplot(
            data=df_sub,
            x='ds',
            y='tree_depth',
            hue='ds',
            palette="muted",
            legend=False,
            ax=axes[1]
        )
        axes[1].set_title('Box Plot: Tree Depth Distribution')
        axes[1].set_xlabel('Dataset')
        axes[1].set_ylabel('Tree Depth')
        axes[1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.show()

        # Create subplots for tree size: violin and box plots
        fig, axes = plt.subplots(1, 2, figsize=(11, 6), sharey=True)

        # Violin plot for tree size
        sns.violinplot(
            data=df_sub,
            x='ds',
            y='tree_size',
            hue='ds',
            palette="muted",
            legend=False,
            inner="quartile",
            cut=0,
            ax=axes[0]
        )
        axes[0].set_title('Violin Plot: Tree Size Distribution')
        axes[0].set_xlabel('Dataset')
        axes[0].set_ylabel('Tree Size')
        axes[0].tick_params(axis='x', rotation=45)

        # Boxplot for tree size
        sns.boxplot(
            data=df_sub,
            x='ds',
            y='tree_size',
            hue='ds',
            palette="muted",
            legend=False,
            ax=axes[1]
        )
        axes[1].set_title('Box Plot: Tree Size Distribution')
        axes[1].set_xlabel('Dataset')
        axes[1].set_ylabel('Tree Size')
        axes[1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.show()

        # Summary statistics
        summary = df_sub.groupby('ds', observed=True).agg(
            depth_mean=('tree_depth', 'mean'),
            depth_95=('tree_depth', lambda x: x.quantile(0.95)),
            size_mean=('tree_size', 'mean'),
            size_95=('tree_size', lambda x: x.quantile(0.95)),
            count=('tree_size', 'count')
        )

        print("\n=== Summary Statistics ===\n")
        print(summary)

        # ---------------------------------------
        # 7. KS-test vs baseline
        # ---------------------------------------
        # baseline = df_sub[df_sub['ds'] == 'BaseLine-DS1']

        # ks_results = {}
        # for g in group:
        #     if g == 'BaseLine-DS1':
        #         continue
        #     subset = df_sub[df_sub['ds'] == g]
            
        #     ks_depth = ks_2samp(baseline['tree_depth'], subset['tree_depth'])
        #     ks_size = ks_2samp(baseline['tree_size'], subset['tree_size'])
            
        #     ks_results[g] = {
        #         'depth_ks_stat': ks_depth.statistic,
        #         'depth_p': ks_depth.pvalue,
        #         'size_ks_stat': ks_size.statistic,
        #         'size_p': ks_size.pvalue
        #     }

        # print("\n=== KS-test vs Baseline ===\n")
        # for model, res in ks_results.items():
        #     print(f"{model}:")
        #     print(f"  Depth KS stat={res['depth_ks_stat']:.3f}, p={res['depth_p']:.3g}")
        #     print(f"  Size  KS stat={res['size_ks_stat']:.3f}, p={res['size_p']:.3g}")
        #     print()         


    def plot_rule_priority_matrix(self, rule_errors_ds, filter=None):
        filtered_df = rule_errors_ds
        
        if filter is not None:
            # Filter the dataset
            filtered_df = rule_errors_ds[rule_errors_ds['ds'].isin(filter)].copy()
            # Enforce the order of 'ds' based on the filter
            filtered_df['ds'] = pd.Categorical(filtered_df['ds'], categories=filter, ordered=True)
            # Sort by the categorical order
            filtered_df = filtered_df.sort_values('ds')
        
        if filtered_df.empty:
            display(Markdown("⚠️ **Warning:** No rule errors were found!"))
            return None
        
        # Aggregate total errors per rule × dataset across all error types
        totals = (
            filtered_df
            .groupby(["rule", "ds"], observed=True)
            .size()
            .reset_index(name="total_errors")
        )

        # Normalize per rule (ratio instead of counts)
        totals["ratio"] = (
            totals["total_errors"] /
            totals.groupby("rule", observed=True)["total_errors"].transform("sum")
        )

        # Pivot for heatmap
        pivot = totals.pivot(index="rule", columns="ds", values="ratio").fillna(0)

        plt.figure(figsize=(14, max(6, len(pivot) * 0.4)))
        sns.heatmap(pivot, cmap="Reds", linewidths=.5, annot=True, fmt=".2f")
        plt.title("Rule Priority Matrix — Overall Error Ratio per Rule per Dataset")
        plt.xlabel("Dataset")
        plt.ylabel("Rule")
        plt.tight_layout()
        plt.show()


class ResultsCoverage():
    def __init__(self, df):
        self.df = df
        self.antlr_error_text_types = [
            # Lexer
            "token recognition error",
            "unterminated string literal",
            "invalid escape sequence",
            "invalid character",
            
            # Parser recognition
            "mismatched input",
            "no viable alternative",
            "missing",
            "extraneous input",
            "required",
            "unwanted token",
            "mismatched token",
            "input mismatch",
            "failed predicate",
            "early exit",
            "missing eof",
        ]       

    def compute_coverage(self, ds):
        # Extract keyword columns (ignore metadata columns)
        meta_cols = ["domain_name", "code", "ds", "kw_extractor"]
        keyword_cols = [col for col in ds.columns if col not in meta_cols]

        # Compute coverage per keyword (1 if appears anywhere)
        coverage = (ds[keyword_cols] > 0).any(axis=0).sort_values(ascending=False)

        coverage_df = pd.DataFrame({
            "keyword": coverage.index,
            "covered": coverage.values
        })
        coverage_df["coverage_rate"] = coverage_df["covered"].astype(int)

        return coverage_df
    
    def compute_coverage_by_ds_extractor(self):
        # Define metadata and keyword columns
        meta_cols = ["domain_name", "code", "ds", "kw_extractor"]
        keyword_cols = [col for col in self.df.columns if col not in meta_cols]

        # Compute coverage per dataset and extractor
        coverage_by_ds_extractor = []

        for (ds_name, extractor), group in self.df.groupby(["ds", "kw_extractor"]):
            used_keywords = (group[keyword_cols] > 0).any(axis=0).sum()
            total_keywords = len(keyword_cols)
            coverage_pct = used_keywords / total_keywords * 100

            coverage_by_ds_extractor.append({
                "ds": ds_name,
                "kw_extractor": extractor,
                "coverage_pct": coverage_pct
            })

        return pd.DataFrame(coverage_by_ds_extractor)
    
    def compute_frequency(self, ds):
        # Extract keyword columns (ignore metadata columns)
        meta_cols = ["domain_name", "code", "ds", "kw_extractor"]
        keyword_cols = [col for col in ds.columns if col not in meta_cols]

        total_freq = ds[keyword_cols].sum().sort_values(ascending=False)
        freq_df = pd.DataFrame({
            "keyword": total_freq.index,
            "total_frequency": total_freq.values
        })
        return freq_df
    
    def filter_kw_extractor_to_regex(self):
        return self.df[self.df["kw_extractor"]=="Regex"]
    
    def filter_kw_extractor_to_lexer(self):
        return self.df[self.df["kw_extractor"]=="Lexer"]

    def filter_kw_extractor_to_parser(self):
        return self.df[self.df["kw_extractor"]=="Parser"]    

    def get_uncovered_keywords(self, ds):
        return ds[ds["covered"] == False]["keyword"].tolist()

    def get_covered_keywords(self, ds):
        return ds[ds["covered"] == True]["keyword"].tolist()

    def get_all_keywords(self, ds):
        return ds["keyword"].tolist()
    

    # def get_grouped_tables(self, df, syntactically_correct_kw_ds, total_kw_ds, grouped_keywords):
    #     exclude = ['domain_name', 'code', 'ds', 'kw_extractor']

    #     total_frequencies = {}
    #     correctly_used = {}

    #     # Loop through each ds group
    #     feature_cols = [c for c in df.columns if c not in exclude]
    #     for ds_value, group in df.groupby('ds'):
    #         lexer = group[group['kw_extractor'] == 'Lexer']
    #         total = lexer[feature_cols].sum(axis=0)
    #         total_frequencies[ds_value] = total

    #     feature_cols = [c for c in syntactically_correct_kw_ds.columns if c not in exclude]
    #     for ds_value, group in syntactically_correct_kw_ds.groupby('ds'):
    #         total = group[feature_cols].sum(axis=0)
    #         correctly_used[ds_value] = total


    #     # --- compute totals directly from total_kw_ds (use same extractor filter if desired) ---
    #     # If you want totals only for Regex extractor, keep the filter; otherwise drop it.
    #     total_by_ds = (
    #         total_kw_ds
    #         .groupby('ds')[feature_cols]
    #         .sum()
    #     )

    #     # --- compute correct counts from syntactically_correct_kw_ds ---
    #     correct_by_ds = (
    #         syntactically_correct_kw_ds
    #         .groupby('ds')[feature_cols]
    #         .sum()
    #     )

    #     # --- align indices/columns so division is safe ---
    #     # Ensure both DataFrames have the same ds index and same columns
    #     all_ds_index = total_by_ds.index.union(correct_by_ds.index)
    #     total_by_ds = total_by_ds.reindex(index=all_ds_index, columns=feature_cols, fill_value=0)
    #     correct_by_ds = correct_by_ds.reindex(index=all_ds_index, columns=feature_cols, fill_value=0)

    #     # --- compute accuracy: correct / total, safely ---
    #     # pandas .div will produce NaN where denom is 0, so fillna(0)
    #     accuracy_df = correct_by_ds.div(total_by_ds).replace([np.inf, -np.inf], 0).fillna(0)

    #     # --- Step 1: Create per-dataset keyword-level table ---
    #     tables_per_ds = {}

    #     for ds_value in total_frequencies.keys():
    #         total = total_frequencies[ds_value]
    #         acc = accuracy_df.loc[ds_value]
            
    #         df_table = pd.DataFrame({
    #             "Keyword": feature_cols,
    #             "Uses": total.values,
    #             "Correctly": acc.values
    #         })
    #         tables_per_ds[ds_value] = df_table
        

    #     # --- Step 2: Group by grouped_keywords ---
    #     grouped_tables = {}

    #     for ds_value, df_table in tables_per_ds.items():
    #         group_rows = []
    #         for group_name, keywords in grouped_keywords.items():
    #             subset = df_table[df_table["Keyword"].isin(keywords)]
    #             if subset.empty:
    #                 uses_fraction = 0.0
    #                 avg_accuracy = 0.0
    #             else:
    #                 used_keywords = (subset["Uses"] > 0)
    #                 uses_fraction = used_keywords.sum() / len(keywords)
    #                 # average accuracy only among used keywords
    #                 if used_keywords.any():
    #                     avg_accuracy = subset.loc[used_keywords, "Correctly"].mean()
    #                 else:
    #                     avg_accuracy = 0.0

    #             group_rows.append({
    #                 "Group": group_name,
    #                 "Uses": round(uses_fraction, 3),
    #                 "Correctly": round(avg_accuracy, 3)
    #             })
            
    #         grouped_tables[ds_value] = pd.DataFrame(group_rows)

    #     return grouped_tables  
    
    def get_grouped_tables(self, df, syntactically_correct_kw_ds, total_kw_ds, grouped_keywords):
        exclude = ['domain_name', 'code', 'ds', 'kw_extractor']

        # Get keyword columns
        feature_cols = [c for c in total_kw_ds.columns if c not in exclude]

        # --- compute totals from total_kw_ds (consistent with KUR/KUC methods) ---
        total_by_ds = (
            total_kw_ds
            .groupby('ds')[feature_cols]
            .sum()
        )

        # --- compute correct counts from syntactically_correct_kw_ds ---
        correct_by_ds = (
            syntactically_correct_kw_ds
            .groupby('ds')[feature_cols]
            .sum()
        )

        # --- align indices/columns so division is safe ---
        all_ds_index = total_by_ds.index.union(correct_by_ds.index)
        total_by_ds = total_by_ds.reindex(index=all_ds_index, columns=feature_cols, fill_value=0)
        correct_by_ds = correct_by_ds.reindex(index=all_ds_index, columns=feature_cols, fill_value=0)

        # --- compute accuracy: correct / total, safely ---
        accuracy_df = correct_by_ds.div(total_by_ds).replace([np.inf, -np.inf], 0).fillna(0)

        # --- Step 1: Create per-dataset keyword-level table ---
        tables_per_ds = {}

        for ds_value in total_by_ds.index:
            total = total_by_ds.loc[ds_value]
            acc = accuracy_df.loc[ds_value]
            
            df_table = pd.DataFrame({
                "Keyword": feature_cols,
                "Uses": total.values,
                "Correctly": acc.values
            })
            tables_per_ds[ds_value] = df_table
        

        # --- Step 2: Group by grouped_keywords ---
        grouped_tables = {}

        for ds_value, df_table in tables_per_ds.items():
            group_rows = []
            for group_name, keywords in grouped_keywords.items():
                subset = df_table[df_table["Keyword"].isin(keywords)]
                if subset.empty:
                    uses_fraction = 0.0
                    avg_accuracy = 0.0
                else:
                    used_keywords = (subset["Uses"] > 0)
                    uses_fraction = used_keywords.sum() / len(keywords)
                    # average accuracy only among used keywords
                    if used_keywords.any():
                        avg_accuracy = subset.loc[used_keywords, "Correctly"].mean()
                    else:
                        avg_accuracy = 0.0

                group_rows.append({
                    "Group": group_name,
                    "Uses": round(uses_fraction, 3),
                    "Correctly": round(avg_accuracy, 3)
                })
            
            grouped_tables[ds_value] = pd.DataFrame(group_rows)

        return grouped_tables


    def get_rule_usage_accuracy_summary_table(self, rule_usage_accuracy_ds): 
        summary_table = (
            rule_usage_accuracy_ds.groupby('ds')['accuracy']
            .describe()[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]
        )
        summary_table = summary_table.reset_index()        
        return summary_table
    

    def get_rule_usage_summary(self, rule_usage_vectors_ds, rule_correct_vectors_ds):
        rule_columns = [c for c in rule_usage_vectors_ds.columns if c != 'ds']

        # Container for per-dataset results
        rules_usage_summary = {}

        # Process each dataset
        for ds_name in rule_usage_vectors_ds['ds'].unique():
            # Filter rows for this dataset
            usage_df = rule_usage_vectors_ds[rule_usage_vectors_ds['ds'] == ds_name]
            correct_df = rule_correct_vectors_ds[rule_correct_vectors_ds['ds'] == ds_name]

            # Count the number of examples (rows) for this dataset
            num_examples = len(usage_df)            
            
            # Sum over all rows — gives total counts per rule
            usage_sum = usage_df[rule_columns].sum()
            correct_sum = correct_df[rule_columns].sum()
            
            # Compute accuracy (avoid division by zero)
            accuracy = np.where(usage_sum == 0, 0, correct_sum / usage_sum)

            # Compute total usage for the dataset
            total_usage = usage_sum.sum()
            
            # Compute usage ratio (avoid division by zero)
            usage_ratio = np.where(total_usage == 0, 0, usage_sum / total_usage)    
            
            # Create summary dataframe
            summary_df = pd.DataFrame({
                'rule': rule_columns,
                'examples': num_examples,
                'usage_count': usage_sum.values,
                'correct_count': correct_sum.values,
                'usage_ratio': usage_ratio,
                'accuracy': accuracy
            })
            
            rules_usage_summary[ds_name] = summary_df      

        return rules_usage_summary
    
    def get_rule_usage_avg_accuracy(self, rules_usage_summary):
        avg_accuracy_per_ds_df = (
            pd.DataFrame([
                {
                    'ds': ds_name,
                    'avg_accuracy': df_item.loc[df_item['usage_count'] > 0, 'accuracy'].mean()
                }
                for ds_name, df_item in rules_usage_summary.items()
            ])
            .sort_values('avg_accuracy', ascending=False)
            .reset_index(drop=True)
        )

        return avg_accuracy_per_ds_df
    
    def get_rule_errors_with_generic_antlr_types(self, rule_errors_ds):

        def detect_antlr_error_type(msg):
            msg_l = (msg or "").lower()
            for e in self.antlr_error_text_types:
                if e in msg_l:
                    return e
            return "unknown"

        # annotate both dataframes with the detected error type and the mapped group
        if rule_errors_ds.empty or "error" not in rule_errors_ds.columns:
            rule_errors_ds["error_type"] = []
        else:
            rule_errors_ds["error_type"] = rule_errors_ds["error"].apply(detect_antlr_error_type)

        return rule_errors_ds
    
    def get_errors_with_generic_antlr_types(self, parser_lexer_errors):

        def detect_antlr_error_type(msg):
            msg_l = (msg or "").lower()
            for e in self.antlr_error_text_types:
                if e in msg_l:
                    return e
            return "unknown"

        if parser_lexer_errors.empty or "msg" not in parser_lexer_errors.columns:
            parser_lexer_errors["error_type"] = []
        else:
            parser_lexer_errors["error_type"] = parser_lexer_errors["msg"].apply(detect_antlr_error_type)


        return parser_lexer_errors    
    
    def get_keyword_coverage_and_correctness_table(self, syntactically_correct_kw_ds, total_kw_ds, ds_filter=None):
        """
        - KUR (Keyword Usage Ratio): proportion of keywords used at least once
        - KUC (Keyword Usage Correctness): weighted ratio of correct keyword uses / total keyword uses
        
        KUR = |keywords with Uses > 0| / |all keywords|
        KUC = Σ(correct_uses) / Σ(total_uses)  [weighted by frequency]
        """
        exclude = ['domain_name', 'code', 'ds', 'kw_extractor']

        # Get keyword columns from total_kw_ds
        feature_cols = [c for c in total_kw_ds.columns if c not in exclude]
        total_keywords_in_language = len(feature_cols)

        # --- compute totals directly from total_kw_ds ---
        total_by_ds = (
            total_kw_ds
            .groupby('ds')[feature_cols]
            .sum()
        )

        # --- compute correct counts from syntactically_correct_kw_ds ---
        correct_by_ds = (
            syntactically_correct_kw_ds
            .groupby('ds')[feature_cols]
            .sum()
        )

        # --- align indices/columns so division is safe ---
        all_ds_index = total_by_ds.index.union(correct_by_ds.index)
        total_by_ds = total_by_ds.reindex(index=all_ds_index, columns=feature_cols, fill_value=0)
        correct_by_ds = correct_by_ds.reindex(index=all_ds_index, columns=feature_cols, fill_value=0)

        # --- Filter datasets if requested ---
        if ds_filter is not None:
            total_by_ds = total_by_ds.loc[total_by_ds.index.isin(ds_filter)]
            correct_by_ds = correct_by_ds.loc[correct_by_ds.index.isin(ds_filter)]

        # --- Calculate KUR and KUC for each dataset ---
        results = []

        for ds_name in total_by_ds.index:
            total_counts = total_by_ds.loc[ds_name]
            correct_counts = correct_by_ds.loc[ds_name]
            
            # KUR: ratio of keywords used at least once
            keywords_used = (total_counts > 0).sum()
            kur = keywords_used / total_keywords_in_language if total_keywords_in_language > 0 else 0
            
            # KUC: weighted ratio (total correct uses / total uses)
            total_uses = total_counts.sum()
            correct_uses = correct_counts.sum()
            kuc = correct_uses / total_uses if total_uses > 0 else 0
            
            results.append({
                'Dataset': ds_name,
                'KUR': round(kur, 4),
                'KUC': round(kuc, 4)
            })
        
        result_df = pd.DataFrame(results)
        result_df = result_df.sort_values('KUC', ascending=False)
        
        return result_df
    
    
    # def get_keyword_coverage_and_correctness_table_v2(self, df, syntactically_correct_kw_ds, total_kw_ds, ds_filter=None):
    #     """
    #     Computes keyword coverage and correctness metrics.
        
    #     - KUR (Keyword Usage Ratio): |keywords used in dataset| / |all keywords in language|
    #     - KUC (Keyword Usage Correctness): average of (correct/total) per keyword, for used keywords only
    #     - SVR (Syntactic Validity Ratio): proportion of examples that parse successfully
    #     """
    #     exclude_cols = ['domain_name', 'code', 'ds', 'kw_extractor']
        
    #     # All keywords in the language (from total_kw_ds columns)
    #     keyword_cols = [c for c in total_kw_ds.columns if c not in exclude_cols]
    #     total_keywords_in_language = len(keyword_cols)
        
    #     # Separate Lexer and Parser data from df for SVR calculation
    #     lexer_df = df[df['kw_extractor'] == 'Lexer']
    #     parser_df = df[df['kw_extractor'] == 'Parser']
        
    #     # Filter datasets if requested
    #     datasets = ds_filter if ds_filter is not None else total_kw_ds['ds'].unique()
    #     results = []
        
    #     for ds_name in datasets:
    #         total_row = total_kw_ds[total_kw_ds['ds'] == ds_name]
            
    #         if total_row.empty:
    #             continue
            
    #         # Sum frequencies across all examples for this dataset
    #         total_counts = total_row[keyword_cols].sum()
            
    #         correct_row = syntactically_correct_kw_ds[syntactically_correct_kw_ds['ds'] == ds_name]
    #         correct_counts = correct_row[keyword_cols].sum() if not correct_row.empty else pd.Series(0, index=keyword_cols)
            
    #         # KUR: count of keywords used at least once / total keywords
    #         used_mask = total_counts > 0
    #         keywords_used = used_mask.sum()
    #         kur = keywords_used / total_keywords_in_language
            
    #         # KUC: average of per-keyword accuracy ratios (only for used keywords)
    #         if keywords_used > 0:
    #             # Per-keyword accuracy: correct / total (only where total > 0)
    #             per_keyword_accuracy = (correct_counts[used_mask] / total_counts[used_mask]).replace([np.inf, -np.inf], 0).fillna(0)
    #             kuc = per_keyword_accuracy.mean()
    #         else:
    #             kuc = 0
            
    #         # SVR: proportion of examples that parse successfully
    #         lexer_data = lexer_df[lexer_df['ds'] == ds_name]
    #         parser_data = parser_df[parser_df['ds'] == ds_name]
            
    #         total_examples = len(lexer_data)
    #         if total_examples > 0 and not parser_data.empty:
    #             # An example parses successfully if Parser found at least one keyword
    #             parser_keyword_sums = parser_data[keyword_cols].sum(axis=1)
    #             parsed_examples = (parser_keyword_sums > 0).sum()
    #             svr = parsed_examples / total_examples
    #         else:
    #             svr = 0
            
    #         results.append({
    #             'Dataset': ds_name,
    #             'KUR': round(kur, 4),
    #             'KUC': round(kuc, 4),
    #             'SVR': round(svr, 4)
    #         })
        
    #     result_df = pd.DataFrame(results)
    #     result_df = result_df.sort_values('SVR', ascending=False)
        
    #     return result_df
    

    def get_keyword_coverage_and_correctness_table_v2(self, df, syntactically_correct_kw_ds, total_kw_ds, rule_usage_vectors_ds, rule_correct_vectors_ds, tree_depth_and_size_ds, ds_filter=None):
        """
        Computes keyword and rule coverage and correctness metrics.
        
        - KCR (Keyword Coverage Rate): |keywords used in dataset| / |all keywords in language|
        - KPV (Keyword Parse Validity): average of (correct/total) per keyword, for used keywords only
        - RCR (Rule Coverage Rate): |rules used in dataset| / |all rules in language|
        - RPV (Rule Parse Validity): average of (correct/total) per rule, for used rules only
        - SVR (Syntactic Validity Ratio): proportion of examples that parse successfully
        - TDM (Tree Depth Mean): average tree depth across examples in dataset
        - TSM (Tree Size Mean): average tree size across examples in dataset
        """
        exclude_cols = ['domain_name', 'code', 'ds', 'kw_extractor']
        
        # All keywords in the language (from total_kw_ds columns)
        keyword_cols = [c for c in total_kw_ds.columns if c not in exclude_cols]
        total_keywords_in_language = len(keyword_cols)
        
        # All rules in the language (from rule_usage_vectors_ds columns)
        rule_cols = [c for c in rule_usage_vectors_ds.columns if c != 'ds']
        total_rules_in_language = len(rule_cols)
        
        # Parser data from df for SVR calculation (bail-out strategy: any keyword > 0 means valid)
        parser_df = df[df['kw_extractor'] == 'Parser']
        
        # Filter datasets if requested
        datasets = ds_filter if ds_filter is not None else total_kw_ds['ds'].unique()
        results = []
        
        for ds_name in datasets:
            # ===== KEYWORD METRICS (KCR, KPV) =====
            total_row = total_kw_ds[total_kw_ds['ds'] == ds_name]
            
            # Sum frequencies across all examples for this dataset
            total_counts = total_row[keyword_cols].sum()
            
            correct_row = syntactically_correct_kw_ds[syntactically_correct_kw_ds['ds'] == ds_name]
            correct_counts = correct_row[keyword_cols].sum() if not correct_row.empty else pd.Series(0, index=keyword_cols)
            
            # KCR: count of keywords used at least once / total keywords
            used_mask = total_counts > 0
            keywords_used = used_mask.sum()
            kcr = keywords_used / total_keywords_in_language if total_keywords_in_language > 0 else 0
            
            # KPV: average of per-keyword accuracy ratios (only for used keywords)
            if keywords_used > 0:
                per_keyword_accuracy = (correct_counts[used_mask] / total_counts[used_mask]).replace([np.inf, -np.inf], 0).fillna(0)
                kpv = per_keyword_accuracy.mean()
            else:
                kpv = 0
            
            # ===== RULE METRICS (RCR, RPV) =====
            rule_usage_row = rule_usage_vectors_ds[rule_usage_vectors_ds['ds'] == ds_name]
            rule_correct_row = rule_correct_vectors_ds[rule_correct_vectors_ds['ds'] == ds_name]
            
            if not rule_usage_row.empty:
                # Sum rule usage across all examples for this dataset
                rule_total_counts = rule_usage_row[rule_cols].sum()
                rule_correct_counts = rule_correct_row[rule_cols].sum() if not rule_correct_row.empty else pd.Series(0, index=rule_cols)
                
                # RCR: count of rules used at least once / total rules
                rule_used_mask = rule_total_counts > 0
                rules_used = rule_used_mask.sum()
                rcr = rules_used / total_rules_in_language if total_rules_in_language > 0 else 0
                
                # RPV: average of per-rule accuracy ratios (only for used rules)
                if rules_used > 0:
                    per_rule_accuracy = (rule_correct_counts[rule_used_mask] / rule_total_counts[rule_used_mask]).replace([np.inf, -np.inf], 0).fillna(0)
                    rpv = per_rule_accuracy.mean()
                else:
                    rpv = 0
            else:
                rcr = 0
                rpv = 0
            
            # ===== SVR (Syntactic Validity Ratio) =====
            # Using Parser with bail-out strategy: if any keyword was found, the example is valid
            parser_data = parser_df[parser_df['ds'] == ds_name]
            
            total_examples = len(parser_data)
            if total_examples > 0:
                # An example is syntactically valid if Parser found at least one keyword
                parser_keyword_sums = parser_data[keyword_cols].sum(axis=1)
                valid_examples = (parser_keyword_sums > 0).sum()
                # print(total_examples,len(parser_keyword_sums), valid_examples, ds_name)
                svr = valid_examples / total_examples
            else:
                svr = 0
            
            # ===== TREE METRICS (TDM, TSM) =====
            tree_data = tree_depth_and_size_ds[tree_depth_and_size_ds['ds'] == ds_name]
            
            if not tree_data.empty:
                tdm = tree_data['tree_depth'].mean()
                tsm = tree_data['tree_size'].mean()
            else:
                tdm = 0
                tsm = 0
            
            results.append({
                'Dataset': ds_name,
                'KCR': round(kcr, 2),
                'KPV': round(kpv, 2),
                'RCR': round(rcr, 2),
                'RPV': round(rpv, 2),
                'SVR': round(svr, 2),
                'TDM': round(tdm, 2),
                'TSM': round(tsm, 2),
            })
        
        result_df = pd.DataFrame(results)
        result_df = result_df.sort_values('SVR', ascending=False)
        
        return result_df