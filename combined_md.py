# # import pandas as pd
# # from pathlib import Path
# # import re

# # def visible_length(text):
# #     """Returns the visible length of text excluding Markdown links."""
# #     return len(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text))

# # def pad_markdown_cell(cell, width, align):
# #     """Pads the cell to match the desired visible width, considering alignment."""
# #     visible = visible_length(cell)
# #     padding = width - visible
# #     if align == 'right':
# #         return ' ' * padding + cell
# #     elif align == 'center':
# #         left = padding // 2
# #         right = padding - left
# #         return ' ' * left + cell + ' ' * right
# #     else:
# #         return cell + ' ' * padding

# # # Paths
# # src_root = Path("/Users/ajoe01/Documents/tim/code-prep-2025")
# # dst_root = Path("/Users/ajoe01/Documents/tim/code-prep-2025-simple")

# # # Process CSVs recursively
# # for src_csv in src_root.rglob("*.csv"):
# #     relative_path = src_csv.relative_to(src_root)
# #     dst_md = src_csv.parent / src_csv.with_suffix(".md").name
# #     dst_md.parent.mkdir(parents=True, exist_ok=True)

# #     df = pd.read_csv(src_csv)

# #     headers = ["Difficulty", "Title", "Frequency", "Acceptance", "Topics"]
# #     alignments = ['left', 'left', 'right', 'right', 'left']
# #     rows = []

# #     for _, row in df.iterrows():
# #         difficulty = str(row['Difficulty'])
# #         title = f"[{row['Title']}]({row['Link']})"
# #         frequency = f"{row['Frequency']:.1f}"
# #         acceptance = f"{row['Acceptance Rate']:.2%}"
# #         topics = str(row['Topics']) if pd.notna(row['Topics']) else ""
# #         rows.append([difficulty, title, frequency, acceptance, topics])

# #     all_rows = [headers] + rows
# #     col_widths = [max(visible_length(str(r[i])) for r in all_rows) for i in range(len(headers))]

# #     def format_row(row):
# #         return "| " + " | ".join(
# #             pad_markdown_cell(str(row[i]), col_widths[i], alignments[i])
# #             for i in range(len(headers))
# #         ) + " |"

# #     # Separator row with proper Markdown alignment specifiers
# #     separator = "| " + " | ".join({
# #         'left':  ':' + '-' * (w - 1),
# #         'center': ':' + '-' * (w - 2) + ':',
# #         'right': '-' * (w - 1) + ':'
# #     }[alignments[i]] for i, w in enumerate(col_widths)) + " |"

# #     lines = [format_row(headers), separator]
# #     lines += [format_row(row) for row in rows]

# #     with open(dst_md, "w", encoding="utf-8") as f:
# #         f.write("\n".join(lines))

# # print("✅ All .csv files converted to clean, readable .md files with aligned tables.")



# import pandas as pd
# from pathlib import Path
# import re

# def visible_length(text):
#     """Returns the visible length of text excluding Markdown links."""
#     return len(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text))

# def pad_markdown_cell(cell, width, align):
#     """Pads the cell to match the desired visible width, considering alignment."""
#     visible = visible_length(cell)
#     padding = width - visible
#     if align == 'right':
#         return ' ' * padding + cell
#     elif align == 'center':
#         left = padding // 2
#         right = padding - left
#         return ' ' * left + cell + ' ' * right
#     else:
#         return cell + ' ' * padding

# # Paths
# src_root = Path("/Users/ajoe01/Documents/tim/code-prep-2025")
# dst_root = Path("/Users/ajoe01/Documents/tim/code-prep-2025")
# dst_root.mkdir(parents=True, exist_ok=True)

# headers = ["Difficulty", "Title", "Frequency", "Acceptance", "Topics"]
# alignments = ['left', 'left', 'right', 'right', 'left']

# for company_dir in src_root.iterdir():
#     if company_dir.is_dir():
#         all_dfs = []
#         # Read and append all CSVs from the company folder
#         for csv_file in company_dir.glob("*.csv"):
#             df = pd.read_csv(csv_file)

#             # Prepare columns similar to your original logic
#             df_processed = pd.DataFrame()
#             df_processed["Difficulty"] = df["Difficulty"].astype(str)
#             df_processed["Title"] = df.apply(lambda row: f"[{row['Title']}]({row['Link']})", axis=1)
#             df_processed["Frequency"] = df["Frequency"].map(lambda x: f"{x:.1f}")
#             df_processed["Acceptance"] = df["Acceptance Rate"].map(lambda x: f"{x:.2%}")
#             if "Topics" in df.columns:
#                 df_processed["Topics"] = df["Topics"].fillna("").astype(str)
#             else:
#                 df_processed["Topics"] = ""

#             all_dfs.append(df_processed)

#         if not all_dfs:
#             continue  # no CSVs found for this company

#         combined_df = pd.concat(all_dfs, ignore_index=True)

#         # Remove duplicates without changing order
#         combined_df = combined_df.drop_duplicates()

#         # Calculate max visible widths for each column including header
#         all_rows = [headers] + combined_df.values.tolist()
#         col_widths = [max(visible_length(str(r[i])) for r in all_rows) for i in range(len(headers))]

#         def format_row(row):
#             return "| " + " | ".join(
#                 pad_markdown_cell(str(row[i]), col_widths[i], alignments[i])
#                 for i in range(len(headers))
#             ) + " |"

#         separator = "| " + " | ".join({
#             'left':  ':' + '-' * (w - 1),
#             'center': ':' + '-' * (w - 2) + ':',
#             'right': '-' * (w - 1) + ':'
#         }[alignments[i]] for i, w in enumerate(col_widths)) + " |"

#         lines = [format_row(headers), separator]
#         lines += [format_row(row) for row in combined_df.values.tolist()]

#         dst_md = dst_root / f"{company_dir.name}.md"
#         with open(dst_md, "w", encoding="utf-8") as f:
#             f.write("\n".join(lines))

# print("✅ Combined markdown files created for each company without duplicates.")

import pandas as pd
from pathlib import Path
import re

def visible_length(text):
    """Returns the visible length of text excluding Markdown links."""
    return len(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text))

def pad_markdown_cell(cell, width, align):
    """Pads the cell to match the desired visible width, considering alignment."""
    visible = visible_length(cell)
    padding = width - visible
    if align == 'right':
        return ' ' * padding + cell
    elif align == 'center':
        left = padding // 2
        right = padding - left
        return ' ' * left + cell + ' ' * right
    else:
        return cell + ' ' * padding

# Paths
src_root = Path("/Users/ajoe01/Documents/tim/code-prep-2025")
dst_root = Path("/Users/ajoe01/Documents/tim/code-prep-2025")
dst_root.mkdir(parents=True, exist_ok=True)

# Add the new "Done" checkbox column as first column
headers = ["Done", "Difficulty", "Title", "Frequency", "Acceptance", "Topics"]
alignments = ['left', 'left', 'left', 'right', 'right', 'left']

for company_dir in src_root.iterdir():
    if company_dir.is_dir():
        all_dfs = []
        # Read and append all CSVs from the company folder
        for csv_file in company_dir.glob("*.csv"):
            df = pd.read_csv(csv_file)

            df_processed = pd.DataFrame()
            df_processed["Difficulty"] = df["Difficulty"].astype(str)
            df_processed["Title"] = df.apply(lambda row: f"[{row['Title']}]({row['Link']})", axis=1)
            df_processed["Frequency"] = df["Frequency"].map(lambda x: f"{x:.1f}")
            df_processed["Acceptance"] = df["Acceptance Rate"].map(lambda x: f"{x:.2%}")
            if "Topics" in df.columns:
                df_processed["Topics"] = df["Topics"].fillna("").astype(str)
            else:
                df_processed["Topics"] = ""

            # Add the checkbox column (unchecked by default)
            df_processed.insert(0, "Done", "[ ]")

            all_dfs.append(df_processed)

        if not all_dfs:
            continue  # no CSVs found for this company

        combined_df = pd.concat(all_dfs, ignore_index=True)
        combined_df = combined_df.drop_duplicates()

        # Calculate max visible widths for each column including header
        all_rows = [headers] + combined_df.values.tolist()
        col_widths = [max(visible_length(str(r[i])) for r in all_rows) for i in range(len(headers))]

        def format_row(row):
            return "| " + " | ".join(
                pad_markdown_cell(str(row[i]), col_widths[i], alignments[i])
                for i in range(len(headers))
            ) + " |"

        separator = "| " + " | ".join({
            'left':  ':' + '-' * (w - 1),
            'center': ':' + '-' * (w - 2) + ':',
            'right': '-' * (w - 1) + ':'
        }[alignments[i]] for i, w in enumerate(col_widths)) + " |"

        lines = [format_row(headers), separator]
        lines += [format_row(row) for row in combined_df.values.tolist()]

        dst_md = dst_root / f"{company_dir.name}.md"
        with open(dst_md, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

print("✅ Combined markdown files with checkboxes created for each company without duplicates.")


