import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import os
import shutil
from datetime import datetime

# Carregar arquivo Excel
file_path = "Cursos realizados.xlsx"  # Substitua pelo caminho correto do arquivo
df = pd.read_excel(file_path, engine="openpyxl")

# Converter colunas de data para datetime
df["Data de início"] = pd.to_datetime(df["Data de início"], format="%d/%m/%Y")
df["Data de conclusão"] = pd.to_datetime(df["Data de conclusão"], format="%d/%m/%Y")

# Título do dashboard
st.title("Dashboard de Cursos")

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Selecione a página",
    [
        "Tabela de Cursos",
        "Gráfico de Carga Horária por Área de Conhecimento",
        "Gráfico de Cursos Concluídos",
        "Exportar",
    ],
)

if page == "Tabela de Cursos":
    # Filtros de data
    first_day_of_current_month = datetime(datetime.now().year, datetime.now().month, 1)
    start_date = st.date_input("Data de início", first_day_of_current_month)
    end_date = st.date_input("Data de conclusão", df["Data de conclusão"].max())

    # Checkbuttons para filtros adicionais
    tipo_curso_options = df["Tipo de curso"].unique().tolist()
    instituicao_options = df["Instituição"].unique().tolist()
    area_conhecimento_options = df["Área de conhecimento"].unique().tolist()
    enviado_options = df["Enviado?"].unique().tolist()

    selected_tipo_curso = st.multiselect("Tipo de curso", tipo_curso_options)
    selected_instituicao = st.multiselect("Instituição", instituicao_options)
    selected_area_conhecimento = st.multiselect(
        "Área de conhecimento", area_conhecimento_options
    )
    selected_enviado = st.multiselect("Enviado?", enviado_options)

    # Filtrar dataframe com base nas datas e checkbuttons selecionados
    filtered_df = df[
        (df["Data de início"] >= pd.to_datetime(start_date))
        & (df["Data de conclusão"] <= pd.to_datetime(end_date))
    ]

    if selected_tipo_curso:
        filtered_df = filtered_df[
            filtered_df["Tipo de curso"].isin(selected_tipo_curso)
        ]

    if selected_instituicao:
        filtered_df = filtered_df[filtered_df["Instituição"].isin(selected_instituicao)]

    if selected_area_conhecimento:
        filtered_df = filtered_df[
            filtered_df["Área de conhecimento"].isin(selected_area_conhecimento)
        ]

    if selected_enviado:
        filtered_df = filtered_df[filtered_df["Enviado?"].isin(selected_enviado)]

    # Exibir dataframe filtrado
    st.dataframe(filtered_df)

    # Informações adicionais
    st.write(f"Total de cursos: {filtered_df.shape[0]}")
    st.write(f"Carga horária total: {filtered_df['Carga horária'].sum()} horas")

    # Mensagem de instrução
    st.write(
        "Use os filtros acima para ajustar as datas de início e conclusão dos cursos exibidos."
    )

    # Botão para exportar o texto para .txt
    if st.button("Exportar para .txt"):
        with open("Cursos realizados.txt", "w") as f:
            for index, row in filtered_df.iterrows():
                f.write(f"Nome do curso: {row['Nome do curso']}\n")
                f.write(f"Instituição: {row['Instituição']}\n")
                f.write(
                    f"Data de início: {row['Data de início'].strftime('%d/%m/%Y')}\n"
                )
                f.write(
                    f"Data de conclusão: {row['Data de conclusão'].strftime('%d/%m/%Y')}\n"
                )
                f.write(f"Carga horária: {row['Carga horária']}\n")
                f.write(f"Planejado? {row['Planejado?']}\n")
                f.write(f"Área de conhecimento: {row['Área de conhecimento']}\n")
                f.write(f"Link: {row['Link']}\n")
                f.write("\n")
        st.write(f"Arquivo exportado com sucesso: Cursos realizados.txt")

elif page == "Gráfico de Carga Horária por Área de Conhecimento":
    # Multiselect for selecting specific areas
    selected_areas = st.multiselect(
        "Selecione as Áreas de Conhecimento", df["Área de conhecimento"].unique()
    )
    if selected_areas:
        df = df[df["Área de conhecimento"].isin(selected_areas)]

    # Gráfico interativo mostrando Carga horária por Área de conhecimento
    carga_horaria_por_area = (
        df.groupby("Área de conhecimento")["Carga horária"].sum().reset_index()
    )

    # Ordenar os dados do maior para o menor pela coluna 'Carga horária'
    carga_horaria_por_area = carga_horaria_por_area.sort_values(
        by="Carga horária", ascending=True
    )

    # Criar o gráfico horizontal
    fig = px.bar(
        carga_horaria_por_area,
        y="Área de conhecimento",
        x="Carga horária",
        labels={"Carga horária": "Carga Horária", "Área de conhecimento": ""},
        title="Carga Horária por Área de Conhecimento",
    )

    # Atualizar o layout para aumentar o tamanho dos rótulos dos eixos
    fig.update_layout(
        yaxis_title="",
        width=1000,
        height=600,
        title_font=dict(size=14),  # Tamanho da fonte do título
        xaxis_title_font=dict(size=14),  # Tamanho da fonte do título do eixo x
        yaxis_title_font=dict(size=14),  # Tamanho da fonte do título do eixo y
        legend_font=dict(size=14),  # Tamanho da fonte da legenda
        font=dict(size=14),  # Tamanho da fonte geral
        xaxis=dict(tickfont=dict(size=14)),  # Tamanho da fonte dos rótulos do eixo x
        yaxis=dict(tickfont=dict(size=14)),  # Tamanho da fonte dos rótulos do eixo y
    )

    st.plotly_chart(fig)

elif page == "Gráfico de Cursos Concluídos":
    # Selectbox for binning options
    binning_option = st.selectbox(
        "Selecione a opção de agrupamento", ["Diário", "Semanal", "Mensal"]
    )

    if binning_option == "Diário":
        df["Binned"] = df["Data de conclusão"].dt.to_period("D").astype(str)
    elif binning_option == "Semanal":
        df["Binned"] = df["Data de conclusão"].dt.to_period("W").astype(str)
    elif binning_option == "Mensal":
        df["Binned"] = df["Data de conclusão"].dt.to_period("M").astype(str)

    # Group by the selected binning option and count the number of concluded courses and sum the hours
    concluded_courses = (
        df.groupby("Binned")
        .agg(
            {
                "Nome do curso": lambda x: "\n".join(x),
                "Data de conclusão": "size",
                "Carga horária": "sum",
            }
        )
        .reset_index()
        .rename(columns={"Data de conclusão": "Número de cursos concluídos"})
    )

    # Create the scatter plot for the number of concluded courses
    scatter_courses = go.Scatter(
        x=concluded_courses["Binned"],
        y=concluded_courses["Número de cursos concluídos"],
        mode="markers",
        name="Número de Cursos Concluídos",
        text=concluded_courses["Nome do curso"],
        hovertemplate="<b>%{x}</b><br>Número de cursos concluídos: %{y}<br>Nome do curso: %{text}",
    )

    # Create the bar plot for the number of hours
    bar_hours = go.Bar(
        x=concluded_courses["Binned"],
        y=concluded_courses["Carga horária"],
        name="Carga Horária",
        opacity=0.6,
    )

    # Create the figure for the number of concluded courses
    fig_courses = go.Figure(data=[scatter_courses])
    fig_courses.update_layout(
        title="Número de Cursos Concluídos ao Longo do Tempo",
        xaxis_title="Tempo",
        yaxis_title="Número de Cursos Concluídos",
        hovermode="x unified",
    )

    st.plotly_chart(fig_courses)

    # Create the figure for the number of hours
    fig_hours = go.Figure(data=[bar_hours])
    fig_hours.update_layout(
        title="Carga Horária ao Longo do Tempo",
        xaxis_title="Tempo",
        yaxis_title="Carga Horária",
        hovermode="x unified",
    )

    st.plotly_chart(fig_hours)

elif page == "Exportar":
    # Assuming df has 'Data de conclusão' and 'Nome arquivo' columns
    df["Data de conclusão"] = pd.to_datetime(df["Data de conclusão"])

    # Filter the DataFrame based on the date range
    start_date = pd.to_datetime(st.date_input("Start date"))
    end_date = pd.to_datetime(st.date_input("End date"))
    filtered_df = df[
        (df["Data de conclusão"] >= start_date) & (df["Data de conclusão"] <= end_date)
    ]

    if st.button("Exportar"):
        # Create export directory if it doesn't exist
        export_dir = f'./Exportados/{start_date.strftime("%Y%m%d")}_{end_date.strftime("%Y%m%d")}'
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        # Copy the files to the export directory
        source_dir = "./Certificados"
        for file_name in filtered_df["Nome arquivo"]:
            source_file = os.path.join(source_dir, f"{file_name}.pdf")
            if os.path.exists(source_file):
                shutil.copy(source_file, export_dir)

        # Create a zip file of the export directory
        zip_file = shutil.make_archive(export_dir, "zip", export_dir)

        # Delete the folder after zipping
        shutil.rmtree(export_dir)

        st.write("Arquivos exportados com sucesso!")
        st.write(f"Arquivo zip criado: {zip_file}")
