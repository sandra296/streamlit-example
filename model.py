{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNhvSe98alHnYDaRERc6YJZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sandra296/streamlit-example/blob/master/model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "6H1C0REG2CtM",
        "outputId": "879f1f2b-526d-4178-aacc-5a99de8f35ad"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     sepal_length  sepal_width  petal_length  petal_width         species\n",
              "0             5.1          3.5           1.4          0.2     Iris-setosa\n",
              "1             4.9          3.0           1.4          0.2     Iris-setosa\n",
              "2             4.7          3.2           1.3          0.2     Iris-setosa\n",
              "3             4.6          3.1           1.5          0.2     Iris-setosa\n",
              "4             5.0          3.6           1.4          0.2     Iris-setosa\n",
              "..            ...          ...           ...          ...             ...\n",
              "145           6.7          3.0           5.2          2.3  Iris-virginica\n",
              "146           6.3          2.5           5.0          1.9  Iris-virginica\n",
              "147           6.5          3.0           5.2          2.0  Iris-virginica\n",
              "148           6.2          3.4           5.4          2.3  Iris-virginica\n",
              "149           5.9          3.0           5.1          1.8  Iris-virginica\n",
              "\n",
              "[150 rows x 5 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-1bb09a81-6179-4e70-ae55-7285f10ab9c1\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "      <th>species</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.6</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>145</th>\n",
              "      <td>6.7</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.3</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>146</th>\n",
              "      <td>6.3</td>\n",
              "      <td>2.5</td>\n",
              "      <td>5.0</td>\n",
              "      <td>1.9</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>147</th>\n",
              "      <td>6.5</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.0</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>148</th>\n",
              "      <td>6.2</td>\n",
              "      <td>3.4</td>\n",
              "      <td>5.4</td>\n",
              "      <td>2.3</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>149</th>\n",
              "      <td>5.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>1.8</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>150 rows × 5 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-1bb09a81-6179-4e70-ae55-7285f10ab9c1')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-1bb09a81-6179-4e70-ae55-7285f10ab9c1 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-1bb09a81-6179-4e70-ae55-7285f10ab9c1');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ],
      "source": [
        "#1.GATHER DATA AND CREATE DATAFRAME\n",
        "import pandas as pd\n",
        "df = pd.read_csv(\"https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/IRIS.csv\")\n",
        "df"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ngdMwwDOg7nT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "21-W4_6X4Dwi",
        "outputId": "ade2080b-1bf1-4918-f9c0-49ec665afaf4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 150 entries, 0 to 149\n",
            "Data columns (total 5 columns):\n",
            " #   Column        Non-Null Count  Dtype  \n",
            "---  ------        --------------  -----  \n",
            " 0   sepal_length  150 non-null    float64\n",
            " 1   sepal_width   150 non-null    float64\n",
            " 2   petal_length  150 non-null    float64\n",
            " 3   petal_width   150 non-null    float64\n",
            " 4   species       150 non-null    object \n",
            "dtypes: float64(4), object(1)\n",
            "memory usage: 6.0+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#preprocessing filtering data\n",
        "df=df.dropna()\n",
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "TB1J-mZpfhPc",
        "outputId": "ba2bb429-f685-4428-b607-8afd55fa8076"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     sepal_length  sepal_width  petal_length  petal_width         species\n",
              "0             5.1          3.5           1.4          0.2     Iris-setosa\n",
              "1             4.9          3.0           1.4          0.2     Iris-setosa\n",
              "2             4.7          3.2           1.3          0.2     Iris-setosa\n",
              "3             4.6          3.1           1.5          0.2     Iris-setosa\n",
              "4             5.0          3.6           1.4          0.2     Iris-setosa\n",
              "..            ...          ...           ...          ...             ...\n",
              "145           6.7          3.0           5.2          2.3  Iris-virginica\n",
              "146           6.3          2.5           5.0          1.9  Iris-virginica\n",
              "147           6.5          3.0           5.2          2.0  Iris-virginica\n",
              "148           6.2          3.4           5.4          2.3  Iris-virginica\n",
              "149           5.9          3.0           5.1          1.8  Iris-virginica\n",
              "\n",
              "[150 rows x 5 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3e2c5539-b3e0-488a-b296-c706f686d956\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "      <th>species</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.6</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>145</th>\n",
              "      <td>6.7</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.3</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>146</th>\n",
              "      <td>6.3</td>\n",
              "      <td>2.5</td>\n",
              "      <td>5.0</td>\n",
              "      <td>1.9</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>147</th>\n",
              "      <td>6.5</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.0</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>148</th>\n",
              "      <td>6.2</td>\n",
              "      <td>3.4</td>\n",
              "      <td>5.4</td>\n",
              "      <td>2.3</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>149</th>\n",
              "      <td>5.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>1.8</td>\n",
              "      <td>Iris-virginica</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>150 rows × 5 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3e2c5539-b3e0-488a-b296-c706f686d956')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3e2c5539-b3e0-488a-b296-c706f686d956 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3e2c5539-b3e0-488a-b296-c706f686d956');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#divide data into input and output\n",
        "x=df.iloc[:,0:4].values\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Aw46t4RIVIKe",
        "outputId": "1ee19c57-451c-4b33-fd5b-bab8ac60ae70"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[5.1, 3.5, 1.4, 0.2],\n",
              "       [4.9, 3. , 1.4, 0.2],\n",
              "       [4.7, 3.2, 1.3, 0.2],\n",
              "       [4.6, 3.1, 1.5, 0.2],\n",
              "       [5. , 3.6, 1.4, 0.2],\n",
              "       [5.4, 3.9, 1.7, 0.4],\n",
              "       [4.6, 3.4, 1.4, 0.3],\n",
              "       [5. , 3.4, 1.5, 0.2],\n",
              "       [4.4, 2.9, 1.4, 0.2],\n",
              "       [4.9, 3.1, 1.5, 0.1],\n",
              "       [5.4, 3.7, 1.5, 0.2],\n",
              "       [4.8, 3.4, 1.6, 0.2],\n",
              "       [4.8, 3. , 1.4, 0.1],\n",
              "       [4.3, 3. , 1.1, 0.1],\n",
              "       [5.8, 4. , 1.2, 0.2],\n",
              "       [5.7, 4.4, 1.5, 0.4],\n",
              "       [5.4, 3.9, 1.3, 0.4],\n",
              "       [5.1, 3.5, 1.4, 0.3],\n",
              "       [5.7, 3.8, 1.7, 0.3],\n",
              "       [5.1, 3.8, 1.5, 0.3],\n",
              "       [5.4, 3.4, 1.7, 0.2],\n",
              "       [5.1, 3.7, 1.5, 0.4],\n",
              "       [4.6, 3.6, 1. , 0.2],\n",
              "       [5.1, 3.3, 1.7, 0.5],\n",
              "       [4.8, 3.4, 1.9, 0.2],\n",
              "       [5. , 3. , 1.6, 0.2],\n",
              "       [5. , 3.4, 1.6, 0.4],\n",
              "       [5.2, 3.5, 1.5, 0.2],\n",
              "       [5.2, 3.4, 1.4, 0.2],\n",
              "       [4.7, 3.2, 1.6, 0.2],\n",
              "       [4.8, 3.1, 1.6, 0.2],\n",
              "       [5.4, 3.4, 1.5, 0.4],\n",
              "       [5.2, 4.1, 1.5, 0.1],\n",
              "       [5.5, 4.2, 1.4, 0.2],\n",
              "       [4.9, 3.1, 1.5, 0.1],\n",
              "       [5. , 3.2, 1.2, 0.2],\n",
              "       [5.5, 3.5, 1.3, 0.2],\n",
              "       [4.9, 3.1, 1.5, 0.1],\n",
              "       [4.4, 3. , 1.3, 0.2],\n",
              "       [5.1, 3.4, 1.5, 0.2],\n",
              "       [5. , 3.5, 1.3, 0.3],\n",
              "       [4.5, 2.3, 1.3, 0.3],\n",
              "       [4.4, 3.2, 1.3, 0.2],\n",
              "       [5. , 3.5, 1.6, 0.6],\n",
              "       [5.1, 3.8, 1.9, 0.4],\n",
              "       [4.8, 3. , 1.4, 0.3],\n",
              "       [5.1, 3.8, 1.6, 0.2],\n",
              "       [4.6, 3.2, 1.4, 0.2],\n",
              "       [5.3, 3.7, 1.5, 0.2],\n",
              "       [5. , 3.3, 1.4, 0.2],\n",
              "       [7. , 3.2, 4.7, 1.4],\n",
              "       [6.4, 3.2, 4.5, 1.5],\n",
              "       [6.9, 3.1, 4.9, 1.5],\n",
              "       [5.5, 2.3, 4. , 1.3],\n",
              "       [6.5, 2.8, 4.6, 1.5],\n",
              "       [5.7, 2.8, 4.5, 1.3],\n",
              "       [6.3, 3.3, 4.7, 1.6],\n",
              "       [4.9, 2.4, 3.3, 1. ],\n",
              "       [6.6, 2.9, 4.6, 1.3],\n",
              "       [5.2, 2.7, 3.9, 1.4],\n",
              "       [5. , 2. , 3.5, 1. ],\n",
              "       [5.9, 3. , 4.2, 1.5],\n",
              "       [6. , 2.2, 4. , 1. ],\n",
              "       [6.1, 2.9, 4.7, 1.4],\n",
              "       [5.6, 2.9, 3.6, 1.3],\n",
              "       [6.7, 3.1, 4.4, 1.4],\n",
              "       [5.6, 3. , 4.5, 1.5],\n",
              "       [5.8, 2.7, 4.1, 1. ],\n",
              "       [6.2, 2.2, 4.5, 1.5],\n",
              "       [5.6, 2.5, 3.9, 1.1],\n",
              "       [5.9, 3.2, 4.8, 1.8],\n",
              "       [6.1, 2.8, 4. , 1.3],\n",
              "       [6.3, 2.5, 4.9, 1.5],\n",
              "       [6.1, 2.8, 4.7, 1.2],\n",
              "       [6.4, 2.9, 4.3, 1.3],\n",
              "       [6.6, 3. , 4.4, 1.4],\n",
              "       [6.8, 2.8, 4.8, 1.4],\n",
              "       [6.7, 3. , 5. , 1.7],\n",
              "       [6. , 2.9, 4.5, 1.5],\n",
              "       [5.7, 2.6, 3.5, 1. ],\n",
              "       [5.5, 2.4, 3.8, 1.1],\n",
              "       [5.5, 2.4, 3.7, 1. ],\n",
              "       [5.8, 2.7, 3.9, 1.2],\n",
              "       [6. , 2.7, 5.1, 1.6],\n",
              "       [5.4, 3. , 4.5, 1.5],\n",
              "       [6. , 3.4, 4.5, 1.6],\n",
              "       [6.7, 3.1, 4.7, 1.5],\n",
              "       [6.3, 2.3, 4.4, 1.3],\n",
              "       [5.6, 3. , 4.1, 1.3],\n",
              "       [5.5, 2.5, 4. , 1.3],\n",
              "       [5.5, 2.6, 4.4, 1.2],\n",
              "       [6.1, 3. , 4.6, 1.4],\n",
              "       [5.8, 2.6, 4. , 1.2],\n",
              "       [5. , 2.3, 3.3, 1. ],\n",
              "       [5.6, 2.7, 4.2, 1.3],\n",
              "       [5.7, 3. , 4.2, 1.2],\n",
              "       [5.7, 2.9, 4.2, 1.3],\n",
              "       [6.2, 2.9, 4.3, 1.3],\n",
              "       [5.1, 2.5, 3. , 1.1],\n",
              "       [5.7, 2.8, 4.1, 1.3],\n",
              "       [6.3, 3.3, 6. , 2.5],\n",
              "       [5.8, 2.7, 5.1, 1.9],\n",
              "       [7.1, 3. , 5.9, 2.1],\n",
              "       [6.3, 2.9, 5.6, 1.8],\n",
              "       [6.5, 3. , 5.8, 2.2],\n",
              "       [7.6, 3. , 6.6, 2.1],\n",
              "       [4.9, 2.5, 4.5, 1.7],\n",
              "       [7.3, 2.9, 6.3, 1.8],\n",
              "       [6.7, 2.5, 5.8, 1.8],\n",
              "       [7.2, 3.6, 6.1, 2.5],\n",
              "       [6.5, 3.2, 5.1, 2. ],\n",
              "       [6.4, 2.7, 5.3, 1.9],\n",
              "       [6.8, 3. , 5.5, 2.1],\n",
              "       [5.7, 2.5, 5. , 2. ],\n",
              "       [5.8, 2.8, 5.1, 2.4],\n",
              "       [6.4, 3.2, 5.3, 2.3],\n",
              "       [6.5, 3. , 5.5, 1.8],\n",
              "       [7.7, 3.8, 6.7, 2.2],\n",
              "       [7.7, 2.6, 6.9, 2.3],\n",
              "       [6. , 2.2, 5. , 1.5],\n",
              "       [6.9, 3.2, 5.7, 2.3],\n",
              "       [5.6, 2.8, 4.9, 2. ],\n",
              "       [7.7, 2.8, 6.7, 2. ],\n",
              "       [6.3, 2.7, 4.9, 1.8],\n",
              "       [6.7, 3.3, 5.7, 2.1],\n",
              "       [7.2, 3.2, 6. , 1.8],\n",
              "       [6.2, 2.8, 4.8, 1.8],\n",
              "       [6.1, 3. , 4.9, 1.8],\n",
              "       [6.4, 2.8, 5.6, 2.1],\n",
              "       [7.2, 3. , 5.8, 1.6],\n",
              "       [7.4, 2.8, 6.1, 1.9],\n",
              "       [7.9, 3.8, 6.4, 2. ],\n",
              "       [6.4, 2.8, 5.6, 2.2],\n",
              "       [6.3, 2.8, 5.1, 1.5],\n",
              "       [6.1, 2.6, 5.6, 1.4],\n",
              "       [7.7, 3. , 6.1, 2.3],\n",
              "       [6.3, 3.4, 5.6, 2.4],\n",
              "       [6.4, 3.1, 5.5, 1.8],\n",
              "       [6. , 3. , 4.8, 1.8],\n",
              "       [6.9, 3.1, 5.4, 2.1],\n",
              "       [6.7, 3.1, 5.6, 2.4],\n",
              "       [6.9, 3.1, 5.1, 2.3],\n",
              "       [5.8, 2.7, 5.1, 1.9],\n",
              "       [6.8, 3.2, 5.9, 2.3],\n",
              "       [6.7, 3.3, 5.7, 2.5],\n",
              "       [6.7, 3. , 5.2, 2.3],\n",
              "       [6.3, 2.5, 5. , 1.9],\n",
              "       [6.5, 3. , 5.2, 2. ],\n",
              "       [6.2, 3.4, 5.4, 2.3],\n",
              "       [5.9, 3. , 5.1, 1.8]])"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y = df.iloc[:,4].values\n",
        "y"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2hJU95rSXtBo",
        "outputId": "742260d8-6fae-40bc-f997-d6d12917e15e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "from pandas.core.common import random_state\n",
        "#train and test variables\n",
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0) "
      ],
      "metadata": {
        "id": "j56uRLkDYAUZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(x.shape)\n",
        "print(x_train.shape)\n",
        "print(x_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SJTgxaKiZ9Fa",
        "outputId": "fa8f1f9d-2103-4b15-b13f-e3e83ec222c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(150, 4)\n",
            "(112, 4)\n",
            "(38, 4)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(y.shape)\n",
        "print(y_train.shape)\n",
        "print(y_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r_eaPcAOaYaQ",
        "outputId": "1287c6c1-02f7-4f77-b378-0a9361b855d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(150,)\n",
            "(112,)\n",
            "(38,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#runregression\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "model=LogisticRegression()"
      ],
      "metadata": {
        "id": "otwYD5VMavK1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#fit the model\n",
        "model.fit(x,y)\n",
        "LogisticRegression()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c4od7aCQbKnx",
        "outputId": "48fb5ab1-ebb1-431a-870e-d6e0ac66d33d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression()"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#predict the output\n",
        "y_pred=model.predict(x)\n",
        "y_pred"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xqxnz0tvcT-I",
        "outputId": "70f38739-ccbb-4da0-b524-42438a80e5c1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-versicolor', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tJTykC9icwb2",
        "outputId": "24f5e8f0-9e89-44e2-d21c-91f8da7fde3e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',\n",
              "       'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',\n",
              "       'Iris-virginica', 'Iris-virginica'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#accuracy\n",
        "from sklearn.metrics import accuracy_score \n",
        "accuracy_score(y_pred,y)*100"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8zFJxUJyc0lu",
        "outputId": "56db8c87-3a13-46ca-cc8c-e6a1b89df68d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "97.33333333333334"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#prediction\n",
        "model.predict([[5.1,3.5,1.4,0.2]])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ntaerEEldxGr",
        "outputId": "acc8c2f0-7d28-42a8-dab6-fd1c3ed91f72"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Iris-setosa'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    }
  ]
}