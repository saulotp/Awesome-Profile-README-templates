{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ds_practice.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMWQ7F9pKFxSwQYwV5BvmrR",
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
        "<a href=\"https://colab.research.google.com/github/saulotp/Awesome-Profile-README-templates/blob/master/ds_practice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pu4z03-40swp"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "employee_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')\n",
        "client_df = pd.read_csv('CadastroClientes.csv', sep='\\t',encoding='latin1')\n",
        "services_df = pd.read_excel('BaseServiçosPrestados.xlsx')"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        },
        "id": "LsPg8LhV1K1p",
        "outputId": "7611083e-08e7-4ae7-92e7-1f41e4779fe8"
      },
      "source": [
        "display(employee_df)\n"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<div>\n",
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
              "      <th>ID Funcionário</th>\n",
              "      <th>Estado Civil</th>\n",
              "      <th>Nome Completo</th>\n",
              "      <th>Salario Base</th>\n",
              "      <th>Impostos</th>\n",
              "      <th>Beneficios</th>\n",
              "      <th>VT</th>\n",
              "      <th>VR</th>\n",
              "      <th>Cargo</th>\n",
              "      <th>Area</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>C</td>\n",
              "      <td>Gabriel Mesquita</td>\n",
              "      <td>21910</td>\n",
              "      <td>10955.0</td>\n",
              "      <td>4382.0</td>\n",
              "      <td>242</td>\n",
              "      <td>719.04</td>\n",
              "      <td>Diretor</td>\n",
              "      <td>Operações</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>C</td>\n",
              "      <td>João Haddad</td>\n",
              "      <td>5404</td>\n",
              "      <td>2702.0</td>\n",
              "      <td>1080.8</td>\n",
              "      <td>154</td>\n",
              "      <td>574.56</td>\n",
              "      <td>Estagiário</td>\n",
              "      <td>Logística</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>C</td>\n",
              "      <td>Amanda Marques Ribeiro</td>\n",
              "      <td>16066</td>\n",
              "      <td>8033.0</td>\n",
              "      <td>3213.2</td>\n",
              "      <td>154</td>\n",
              "      <td>729.12</td>\n",
              "      <td>Estagiário</td>\n",
              "      <td>Administrativo</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>C</td>\n",
              "      <td>Guilherme Nunez</td>\n",
              "      <td>21305</td>\n",
              "      <td>10652.5</td>\n",
              "      <td>4261.0</td>\n",
              "      <td>220</td>\n",
              "      <td>524.16</td>\n",
              "      <td>Analista</td>\n",
              "      <td>Administrativo</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>C</td>\n",
              "      <td>Adelino Gomes</td>\n",
              "      <td>5098</td>\n",
              "      <td>2549.0</td>\n",
              "      <td>1019.6</td>\n",
              "      <td>176</td>\n",
              "      <td>725.76</td>\n",
              "      <td>Analista</td>\n",
              "      <td>Administrativo</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>109</th>\n",
              "      <td>143</td>\n",
              "      <td>C</td>\n",
              "      <td>Renan Scharnhorst Ott</td>\n",
              "      <td>10793</td>\n",
              "      <td>5396.5</td>\n",
              "      <td>2158.6</td>\n",
              "      <td>242</td>\n",
              "      <td>514.08</td>\n",
              "      <td>Analista</td>\n",
              "      <td>Logística</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>110</th>\n",
              "      <td>144</td>\n",
              "      <td>S</td>\n",
              "      <td>Lucas Brum Pereira</td>\n",
              "      <td>4048</td>\n",
              "      <td>2024.0</td>\n",
              "      <td>809.6</td>\n",
              "      <td>198</td>\n",
              "      <td>796.32</td>\n",
              "      <td>Estagiário</td>\n",
              "      <td>Comercial</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>111</th>\n",
              "      <td>148</td>\n",
              "      <td>S</td>\n",
              "      <td>Caio Stellet</td>\n",
              "      <td>24596</td>\n",
              "      <td>12298.0</td>\n",
              "      <td>4919.2</td>\n",
              "      <td>242</td>\n",
              "      <td>561.12</td>\n",
              "      <td>Analista</td>\n",
              "      <td>Administrativo</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>112</th>\n",
              "      <td>149</td>\n",
              "      <td>C</td>\n",
              "      <td>Fernanda Rocha</td>\n",
              "      <td>5078</td>\n",
              "      <td>2539.0</td>\n",
              "      <td>1015.6</td>\n",
              "      <td>308</td>\n",
              "      <td>665.28</td>\n",
              "      <td>Estagiário</td>\n",
              "      <td>Comercial</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>113</th>\n",
              "      <td>150</td>\n",
              "      <td>C</td>\n",
              "      <td>Eduardo Brum</td>\n",
              "      <td>15939</td>\n",
              "      <td>7969.5</td>\n",
              "      <td>3187.8</td>\n",
              "      <td>220</td>\n",
              "      <td>769.44</td>\n",
              "      <td>Analista</td>\n",
              "      <td>Comercial</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>114 rows × 10 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     ID Funcionário Estado Civil  ...       Cargo            Area\n",
              "0                 1            C  ...     Diretor       Operações\n",
              "1                 2            C  ...  Estagiário       Logística\n",
              "2                 3            C  ...  Estagiário  Administrativo\n",
              "3                 4            C  ...    Analista  Administrativo\n",
              "4                 5            C  ...    Analista  Administrativo\n",
              "..              ...          ...  ...         ...             ...\n",
              "109             143            C  ...    Analista       Logística\n",
              "110             144            S  ...  Estagiário       Comercial\n",
              "111             148            S  ...    Analista  Administrativo\n",
              "112             149            C  ...  Estagiário       Comercial\n",
              "113             150            C  ...    Analista       Comercial\n",
              "\n",
              "[114 rows x 10 columns]"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "52GYTZiu5b2M",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0308e5dc-fe2a-4a15-f220-a17b6bb489ec"
      },
      "source": [
        "payroll_df = employee_df['Salario Base'] + employee_df['Impostos'] + employee_df['Beneficios'] + employee_df['VT']+ employee_df['VR']\n",
        "payroll_df = payroll_df.sum()\n",
        "print(f'R$ {payroll_df:,.2f}')"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "R$ 2,717,493.22\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 436
        },
        "id": "VSFEo6Z9GTcl",
        "outputId": "de878f38-247d-4c2a-9cdf-21e1b22ec488"
      },
      "source": [
        "services_df = pd.merge(services_df, client_df)\n",
        "services_df = services_df.drop(['Unnamed: 3'], axis=1)\n",
        "\n",
        "display(services_df)\n",
        "\n",
        "revenue_df = services_df['Tempo Total de Contrato (Meses)'] * services_df['Valor Contrato Mensal'] \n",
        "revenue_df = revenue_df.sum()\n",
        "print(f'R$ {revenue_df:,.2f}')"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<div>\n",
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
              "      <th>Codigo do Servico</th>\n",
              "      <th>ID Funcionário</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>Tempo Total de Contrato (Meses)</th>\n",
              "      <th>Cliente</th>\n",
              "      <th>Valor Contrato Mensal</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>OS0001</td>\n",
              "      <td>67</td>\n",
              "      <td>1</td>\n",
              "      <td>14</td>\n",
              "      <td>Teixeira Gonçalves</td>\n",
              "      <td>540</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>OS0002</td>\n",
              "      <td>17</td>\n",
              "      <td>2</td>\n",
              "      <td>12</td>\n",
              "      <td>Souza Santos</td>\n",
              "      <td>1260</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>OS0003</td>\n",
              "      <td>116</td>\n",
              "      <td>4</td>\n",
              "      <td>14</td>\n",
              "      <td>Santos Costa</td>\n",
              "      <td>2520</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>OS0004</td>\n",
              "      <td>37</td>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>Do Monteiro</td>\n",
              "      <td>3510</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>OS0005</td>\n",
              "      <td>130</td>\n",
              "      <td>6</td>\n",
              "      <td>8</td>\n",
              "      <td>Soares Lobo</td>\n",
              "      <td>2340</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>232</th>\n",
              "      <td>OS0233</td>\n",
              "      <td>111</td>\n",
              "      <td>315</td>\n",
              "      <td>4</td>\n",
              "      <td>Americo Bomfim</td>\n",
              "      <td>1575</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>233</th>\n",
              "      <td>OS0234</td>\n",
              "      <td>124</td>\n",
              "      <td>316</td>\n",
              "      <td>8</td>\n",
              "      <td>Manoel Costa</td>\n",
              "      <td>3690</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>234</th>\n",
              "      <td>OS0235</td>\n",
              "      <td>72</td>\n",
              "      <td>317</td>\n",
              "      <td>6</td>\n",
              "      <td>Gomes Machado</td>\n",
              "      <td>2385</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>235</th>\n",
              "      <td>OS0236</td>\n",
              "      <td>90</td>\n",
              "      <td>319</td>\n",
              "      <td>14</td>\n",
              "      <td>Pereira Fazenda</td>\n",
              "      <td>4185</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>236</th>\n",
              "      <td>OS0237</td>\n",
              "      <td>22</td>\n",
              "      <td>320</td>\n",
              "      <td>12</td>\n",
              "      <td>Americo Damasceno</td>\n",
              "      <td>2430</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>237 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "    Codigo do Servico  ...  Valor Contrato Mensal\n",
              "0              OS0001  ...                    540\n",
              "1              OS0002  ...                   1260\n",
              "2              OS0003  ...                   2520\n",
              "3              OS0004  ...                   3510\n",
              "4              OS0005  ...                   2340\n",
              "..                ...  ...                    ...\n",
              "232            OS0233  ...                   1575\n",
              "233            OS0234  ...                   3690\n",
              "234            OS0235  ...                   2385\n",
              "235            OS0236  ...                   4185\n",
              "236            OS0237  ...                   2430\n",
              "\n",
              "[237 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "R$ 5,519,160.00\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "CTk-81sPJRik",
        "outputId": "37bf38d9-672c-4363-d092-27191955e3bf"
      },
      "source": [
        "display(revenue_df)"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "5519160"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        },
        "id": "UU131KHGMZbo",
        "outputId": "9543e80d-5002-445a-e351-28210d0e5f71"
      },
      "source": [
        "display(services_df)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<div>\n",
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
              "      <th>Codigo do Servico</th>\n",
              "      <th>ID Funcionário</th>\n",
              "      <th>ID Cliente</th>\n",
              "      <th>Tempo Total de Contrato (Meses)</th>\n",
              "      <th>Cliente</th>\n",
              "      <th>Valor Contrato Mensal</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>OS0001</td>\n",
              "      <td>67</td>\n",
              "      <td>1</td>\n",
              "      <td>14</td>\n",
              "      <td>Teixeira Gonçalves</td>\n",
              "      <td>540</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>OS0002</td>\n",
              "      <td>17</td>\n",
              "      <td>2</td>\n",
              "      <td>12</td>\n",
              "      <td>Souza Santos</td>\n",
              "      <td>1260</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>OS0003</td>\n",
              "      <td>116</td>\n",
              "      <td>4</td>\n",
              "      <td>14</td>\n",
              "      <td>Santos Costa</td>\n",
              "      <td>2520</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>OS0004</td>\n",
              "      <td>37</td>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>Do Monteiro</td>\n",
              "      <td>3510</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>OS0005</td>\n",
              "      <td>130</td>\n",
              "      <td>6</td>\n",
              "      <td>8</td>\n",
              "      <td>Soares Lobo</td>\n",
              "      <td>2340</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>232</th>\n",
              "      <td>OS0233</td>\n",
              "      <td>111</td>\n",
              "      <td>315</td>\n",
              "      <td>4</td>\n",
              "      <td>Americo Bomfim</td>\n",
              "      <td>1575</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>233</th>\n",
              "      <td>OS0234</td>\n",
              "      <td>124</td>\n",
              "      <td>316</td>\n",
              "      <td>8</td>\n",
              "      <td>Manoel Costa</td>\n",
              "      <td>3690</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>234</th>\n",
              "      <td>OS0235</td>\n",
              "      <td>72</td>\n",
              "      <td>317</td>\n",
              "      <td>6</td>\n",
              "      <td>Gomes Machado</td>\n",
              "      <td>2385</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>235</th>\n",
              "      <td>OS0236</td>\n",
              "      <td>90</td>\n",
              "      <td>319</td>\n",
              "      <td>14</td>\n",
              "      <td>Pereira Fazenda</td>\n",
              "      <td>4185</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>236</th>\n",
              "      <td>OS0237</td>\n",
              "      <td>22</td>\n",
              "      <td>320</td>\n",
              "      <td>12</td>\n",
              "      <td>Americo Damasceno</td>\n",
              "      <td>2430</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>237 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "    Codigo do Servico  ...  Valor Contrato Mensal\n",
              "0              OS0001  ...                    540\n",
              "1              OS0002  ...                   1260\n",
              "2              OS0003  ...                   2520\n",
              "3              OS0004  ...                   3510\n",
              "4              OS0005  ...                   2340\n",
              "..                ...  ...                    ...\n",
              "232            OS0233  ...                   1575\n",
              "233            OS0234  ...                   3690\n",
              "234            OS0235  ...                   2385\n",
              "235            OS0236  ...                   4185\n",
              "236            OS0237  ...                   2430\n",
              "\n",
              "[237 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K430x4eLLyXd",
        "outputId": "1957b738-c825-403d-afb2-601a908492e9"
      },
      "source": [
        "employeecount_df = len(services_df['ID Funcionário'].unique())\n",
        "employeetotalcount_df = len(employee_df['ID Funcionário'])\n",
        "print(f'{employeecount_df*100/employeetotalcount_df:.2f}%')"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "86.84%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CjAAqqW_Qk6m",
        "outputId": "19e82ed3-ee2f-45c1-a6f1-b2df53a9aecf"
      },
      "source": [
        "area_df = pd.merge(services_df, employee_df)\n",
        "print(area_df['Area'].value_counts())"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Administrativo    63\n",
            "Operações         48\n",
            "Comercial         44\n",
            "Financeiro        42\n",
            "Logística         40\n",
            "Name: Area, dtype: int64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "k3ep1_UYR2db",
        "outputId": "5d8bb411-32cc-4ecc-f504-71fd66d77f7e"
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "areaplot = area_df['Area'].value_counts()\n",
        "areaplot.plot(kind='pie')"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f24f0e405d0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAASIAAADnCAYAAAC67FsFAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3deXxU9dn38c+VnXXYkX0AwURWZXEFNdrtxu5Wa1sb76etXVJb7Zqu5q7W4mOXx9Zbc6utosVqq3VrvF3qgqAiiAoDBkUFQWUTBIUkk2Tmev44JxpjQibJzPxm5lzv1ysvYHLO+V0Jk2/O8ltEVTHGGJfyXBdgjDEWRMYY5yyIjDHOWRAZY5yzIDLGOGdBZIxxzoLIGOOcBZExxjkLImOMcxZExhjnLIiMMc5ZEBljnLMgMsY4Z0FkjHHOgsgY45wFkTHGOQsiY4xzFkTGGOcsiIwxzlkQGWOcsyAyxjhnQWSMcc6CyBjjnAWRMcY5CyJjjHMWRMYY5yyIjDHOFbguwGSg6lA/IAyMA8aVR387+BUdPR4Y7n8Mw3vvKBD3/2z/9xjwJvBaBx/btixe9E4avyKT4URVXddgXKkOCTAJmAXM9D9mARMBad3snKaq9cvjM6cnufV3gK3AWmAl8BTw7JbFi5qT3I7JAhZEQVIdygfmAqcBpwLzgP5d7faL5nNX3hT78LEprg6gEXgWL5RWAk9tWbxoSxraNY7ZpVmuqw4dAXwIL3xOBkLdPcRE2dGU5Ko6UwIc538AEK6q3Q7cC9wJ/HvL4kWNaarFpJGdEeWi6tBE4Av+x5G9PdxDsaOWfaX5hyf1uq7eOwjcD9wG3L1l8aKDjusxSWJBlCuqQyOAs/DCJ6mXUXXx8Ss+1rT4xGQeMwkOAncDfwPus3tL2c2CKNtVh04FLgA+BuSnoondGnpmXvTqo1Nx7CTZDlwJ1GxZvGiv62JM91kQZaPqUBHemc+FeE+6UqpRCzeVRpdMSXU7SVAPXA/8YcviRS+7LsYkzoIom1SHhgHfBL4FHJauZuPKW5OiNw9OV3tJEAfuAn63ZfGix10XY7pmQZQNqkMDgR/hnQH1dVHC1MYl0SYKi1203Usrgf+7ZfGiO1wXYjpnQZTJvEuwbwI/x+vN7MxJ0d+//qoeNsZlDb20DPjulsWL1rouxHyQBVEm8no8fx64BK/ns3NfavpJZEV8xgzXdfRSDLgW+PmWxYv2uC7GvMfZoFcRGSsid4nIJhF5WUSuEJEiR7VcLCIrReQfIjLNRQ3vqg4dBawCbiZDQghgouzIhT47+cA3gE3hqtrzw1W1Se/QKyKfEhEVkdJOPv+oiMztxvHmisgfE9juiS4+/9NE22y33wUi0rfNv+8VkUE9OdahOAkiERHgn8CdqjoFmIo31ODXSTh2tx9hq+ovVPVYVf2cqm7obQ09Uh0qoTr0G7wQSviNmi5h2RF1XUMSDQb+CDwXrqo9NcnHPhtY4f/Za6r6tKp+J4Htju9ikw6DSDyHyoELaHNfUlX/Q1X3dVVPd7k6IyoHGlX1egBVjeHdiP0/IvIt/0zpUf9s6aLWnUTkSyKySkSeE5H/aQ0dETkgIr8TkbXAcSLySxFZLSLrReQaP/gQkcNF5N8islZE1ojIOBEpEZHrRSQiIs+KyCn+tvkicrl/nHUi8nX/9VEi8phfw3oRWdDr70Z16ETgOaCKDB12M0F2ui4hFaYB/w5X1f4tXFXb7aEv7YlIf+BE4Ct4l9aISB8RuUVE6kTkDqBPm+0P+O+xDf77cr7/vn9FRD7hb3OyiPzL/3u1iPylzTbfaXss/88PvD9FZDHQx39tqYiEReQFEbkRWA+ME5GrReRpv5b/8o/1HWA08IiIPOK/tkVEhonIYhGpbNN+tYj8wA+2y/22IyJyViLfO1dBNA1Y0/YFVX0bbzR2ATAf+CxeH5nP+aenZXg9h09Q1dl41/tf9HfvBzylqrNUdQVwparOU9XpeP/xp/vbLQWuUNVZeG+YN4FKIE9VZ+D9FlsiIiV4b6b9qjoPb3Do10SkdejE/X4Ns/ACpGeqQ/2pDl0JPAYc0ePjpMFoeTMlnSUzxOfxzo562yP9k8B9qvoisEdE5uA9bKhX1TLgImBOm+37AQ+r6jS82QguwRsX+GngV520UQp8BO9n5CIRKWz3+Q+8P1W1CmhQ1dmq2vozMwW4SlWnqeqrwM9UdS7ez9xJIjJTVf8IvAGcoqqntGvnVuDMNv8+03/tM0Br26cBl4vIqEN90yBDf/sCD6rqHgAR+SdeaLTg/Seu9k9w+gC7/O1jwO1t9j9FRH6Ed0o5BNggIo8CY1T1HgBVbfCPfyJer1xUdaOIvIp3qfhhYKaInOEfM4T3n7ca+Iv/BrhTVXsWRN69oNvIoPtAhzJM9vfpequsFgaWh6tqfwlctmXxongPjnE2cIX/91v8fx+OdxmIqq4TkXVttm8C7vP/HgGiqtosIhG/no7UqmoUiIrILmAk3hxPrRJ9f76qqivb/PtMETkPLxNG4Y1RXNfhnt7X8qyIjBCR0XhzVL2lqttE5HvA3/yrnJ0isgzvF/ndnR0L3J0RPc/7fzMgIgOB8XiB0/5RnuLNj7PET/XZqnqEqlb7n2/0v3D8s5mrgDP8s5xr8UZ1H0pHjw4FOL9NexNV9QFVfQxYCLwO3CAiX07wa35PdeirwBNkSQgBDKBhoOsa0qAAuBS4P1xV260OoyIyBO+Ww3UisgX4Id5Zghxit2Z977F1HIgCqGqczk8S2t6ri7Xfrhvvz3cfPvhn+j8ATlXVmUAtXf/MAPwDOAPvSuXWBLbvlKsgegjo2/pN8u/1/A64Aa+b/odEZIiI9AE+BTzu73OGiIzw9xkiIhM6OHbrN/BN/5r9DABVfQd4TUQ+7u/fxz/+cvxLPBGZiheGL+CN8v5m66mviEwVkX5+mztV9VrgOiDxMVjVoT5Uh64nsXDMKMU0D3VdQxqdBqwNV9V+tBv7nAHcpKoTVDWsquOAzXi3IL4AICLTSfGQnEO8P5s7uIxrNRAvmPaLyEi8cYut3gEGdLLfrXiXtWfghRJ4P09n+fdYh+OF4qqu6nYSRP5vgU/j3f/ZBLyINylW6539VXiXWuuA2/0nB8/jdex7wD+9fRDvFLL9sffh/aCvxwuT1W0+fQ7wPRHZjvcNG4p39pTnnw7fCpzrn/peh3fm9oyIrAf+B++3z8nAWhF5Fu83wRUkojp0OPAkcG5C22eYPNEhhbSka16iTDACuDdcVXt5uKo2kZ+Ts4H2vbdvx5vtsr+I1OHd91nTfsckO5mO35/XAOtEZGn7HVR1Ld6EdBvxuo20HRZzDXBf683qdvttwAup11V1u//yHXg/t2uBh4EfqeqOrorOuA6NInIuMFdVv53CNr4AbFfVD3xzU6I69GHg7/RgUrJMsjD6h9e26sixrutw4G7g7C2LF9W7LiRXBW4VDxH5PnAxKZoy4wOqQ+fiXXNndQgBjJddSe8/kiU+ATwarqod4bqQXJVxQaSqN6TybEhVf6eqk1X136lq413VoV/gTUuRqU8nuyUsOw64rsGhecDKcFXtVNeF5KKMC6KcUB0SqkNX0HlfkKwUTt/c1ZlqIt4j/lmuC8k1FkTJVh0qAJYAXXbLzzYTZGdP+tbkmhF4l2ldDakw3WBBlEzVoTy8EDrHdSmpMFr25MQlZhIMAh4MV9We5rqQXGFBlFxX4fcZyUXDZX9W9X1Ksb7AneGq2nmuC8kFFkTJUh26DPi66zJSaQD1Wf/kL8n6AbXhqtrDXReS7SyIkqE69FO8qVxzWjHNQ1zXkIGG4w0JsUf7vWBB1FvVoW+ThHmUsoEQuN7ViZqE1wu7y+W7TccsiHqjOvRx/JHVQSCCHCZ7d7uuI0PNAW4PV9V2Np7LHIIFUU95a8r/lUOPrs45Ae5dnYgPA38OV9UG6j2RDBZEPeEt73Mn3qjlQAl47+pEnAP8l+siso0FUXd5K2zchDdTXuBMzK25q1PlZymYCzunWRB130V4gyADaYLszKzpGjJTHnBTuKrW6Vp02cSCqDuqQx8Dfum6DJdyfO7qZBqFN+DZJMCCKFHVoSHAnwnYzen2AjB3dTKdHq6qTdlMErnEgihxV9LBjJBBM5D6zqYNNR27PFxVm9LpYXOBBVEiqkOfJUkL5mW7gM1dnQwlwC3hqlo7kzwEC6KuVIdGAFe7LiNTCDqkgJZm13VkmTLgD66LyGQWRF2rwRtPZPB6V4+y3tU9cV4SFnDMWRZEh1Id+hTeaiOmjXGy6y3XNWQhAa6wXtcdsyDqTHWoCPit6zIykfWu7rH55Oikeb1lQdS57wKTXReRicLWu7o3fhOuqu3nuohMY0HUkerQcLzFHE0HrHd1r4zmvYVEjc+CqGMXE8ABrYkaa72re+t74arasOsiMokFUXvVoRnAV12XkcmG2dzVvVUCXO66iExiQfRB6VsFNksNpN7OFnvvjHBV7ULXRWQKC6K2qkNHEuCR9YmyuauT5heuC8gUFkTv92MCPqg1EYIOtd7VSXFauKr2aNdFZAILolbVoXHYeLKEeHNXv2W9q5Mj51d/SYQF0Xu+D9jE5wmy3tVJc0a4qjbw/dUsiACqQ0OxJ2XdYr2rkyYfCPycRRZEnq/jrdppEmRzVyfVfwa9t7UFkec/XReQbSbIzrjrGnJIiICPQbMgqg6dCNja5d00Rt4scF1Djql0XYBLFkRwrusCspH1rk666eGq2jmui3Al2EFUHeoLfM51GdloIAetd3XyfdZ1Aa4EO4jgM9jg1h4poXmw6xpykAVRQH3ZdQHZStBh+cRaXNeRY6aGq2qnuy7CheAGUXVoEHCK6zKylc1dnTKfcV2AC8ENIvgQYE9+emGs7NrruoYcFMjLsyAH0cdcF5DtJsqOg65ryEEzw1W1getOEswgqg4J8FHXZWS7sOxodF1DjgrcWVEwgwhmY8tH95rNXZ0ygVvCKqhBZJdlSTBG3gzq+yfV5oSragPVYTSob6SPuC4gFwyX/baee2oUAIGaMC14QVQdKgDmuS4jFwykfoDrGnLYMa4LSKfgBRHMBOw3eRKU0DTUdQ05bL7rAtIpcEH0jkhgBxYmm6BDrXd1ygQqiALXoe/48Lhj8lR3Do/FXp0VbWpYUN/Q9/iGxgkjYrERrmvLNiLIYex983WGH+a6lhw0KVxVO2zL4kVvui4kHQIXRMBRcZGROwsKRj5QUMAD/foCkKe6Y2QstnVWY7RhQUND3+MbGsPDYvHhjmvNeGNl997X1YIoReYD97ouIh0CFUQzlswoAKZ19Lm4yGHbCwoO296/gPv6e7N25qtuH9kS2zo7Gm1cWN/Q79iGxvDQeHxYOmvOdOG8HQeeih3puoxcZUGUoyYBxYluHBMZ9UZhwag3Cgu4971wen1US2zbUY3R6IKGhv7HNjROHByPB3bBwUk2d3UqBeZ+ZtCCaGJvDxATGfNaYcGY1woLuGfAu+H02uiWlteOboxGF9Y3DDimMTopFI8P6nW1WWCC7Iy5riGHjXddQLoELYjCqThoTGTstsLCsdsKC7lrQH8AClS3jm5peX1OYzS6oL4hNL+xcVIorqFUtO+SzV2dUmNcF5AuQXsThdPVUIvI+K2FheO3FhZyx4D+oKoF8OrY5pY35jRGmxY0NITmNzROGqCa1TNEDpd9CV/qmm4bGq6qLdmyeFHODy62IEoXEWmBCVuKCidsKSrk9oFeOBXC5rHNLdvnNjY2L6xvHDS3sXFSf9Ws6bE8kPqsDtIsMBp4xXURqZa2IBKREcC7A/lUdWu62m4j7KDNzolIM0zcXFQ4cXNRIf8YOABU44WweXxz8/Z5jdHmBfUNg+c2Rif3Vc3IBfiKaQrsjfo0GYMFUe+JyCeA3+El+y5gAlBHJ4/RU2ysgza7RySvGSa+XFQ08eWiIm7xw6lIeXlCS/OOeQ3RlgUNDUPmNEYn91Ht67rcPL93dYz8oJ1dp0sg7hOl481zMXAs8G9VPUpETgG+lIZ2O5KdN4tF8pqEyZuKiiZvKiri5tAAUI0Vq740obllx/zGxvjC+sYhR0Wjk0tU0zqOToS8kby18w2G2fxOqTHadQHpkI4galbVPSKSJyJ5qvqIiPy/NLT7PjOWzBCgf7rbTRmR/KjI4S8WFx3+YnERfw0NBNWWYtVNE5tbdnrh1DB0djQ6uVhJ6dw242TXW2+oBVGK2BlRkuwTkf7AcmCpiOwCXMx13B8QB+2mj0hBVGTKxuKiKRuLi7jRD6cS1RcnNrfsPKahkYUNDUNnNUYnF3WjY2dXJuTttN7VqROIgE9HEH0SaAAuAL6Id3n0qzS0214wn+6IFDSKTK0rLppaV1zEDYMGgmpzH9WNk5qbdx/b0MiC+sZhM6LRyUVQ1JMmJlrv6lQKxEyNKQ8iVT0oIhOAKaq6RET6AvmpbrcDWfNIPOVEChtESjcUF5duKC7mz4NCoNrUV7VuclPz7mMbG2VhfcPwadGmyYVQ2NXhrHd1SgXiIUA6npp9DTgPGAJMxrvmrQFOTXXb7eTO/aFUECmqFymLlBSXRUqKudYLp2g/1ecnNzXvOb6hURY0NAw/Mto0uaDd+2as7HbxiyUoLIiSpBJvFPFTAKq6ye9TZDKdSPFBkSPXlRSzrqSYmsEhUG3sp/rClKbmPcc3NOQtqG8cOTj6do8u6UxCujwjzQXpCKKoqjaJePeJRaQAcLEMTbODNnOPSMlBkWnPlRTzXEkxVw2G8+8uuv8Hw4o3I5Kd3SMyWBzqXdeQDukIomUi8lOgj4h8CPgWcE8a2m2vyUGbOW/mK/HIiRvqT3txyvIVr4856STX9eSa/IDcrE7HnNU/BnYDEeDreBM9/TwN7bZnZ0RJVtykB6v+ER8okD/lpduOl3jLq65rykGBeBCQ0jMiEckHNqhqKXBtKttKgAVRkv3yb7FnCuIsAMjTeOGUl27b8eLUz09wXVeOCcSlWUrPiFQ1BrwgIpkwwZNdmiXRiRviT095wwuhVmPfWH5MQfPBta5qylFvuS4gHdJxaTYY2CAiD4nI3f7HXWlot723HbSZk/rX61vfvic+rqPPzVh/TSGqLh5G5CoLoiT5BXA6Xm/q3wOrgcPT0O77RCoiB4ED6W43F11yY2xjnjKyo88N3v/SkX3rdzyR7ppymAVRMqjqMryzkdOBG4ByvA6NLux01G7OOP2p+BOj3+K4Q20zK3LVRFQb0lVTjtvruoB0SFkQichUEblIRDYCfwK2AqKqp6jqn1LVbhd2OGo3Jwzdr9vPeTje5ejWPo17Rw/bE3kqHTUFgJ0R9dJGvLOf01X1RD98XD+KtCDqhUuXxN4QSGh1kiPrbpiDxnenuqYAcDGTadqlMog+A2wHHhGRa0XkVNxPw2FB1ENfeij22OCDia+zVRCLDpiw9cGNqawpIHJ+mlhIYRCp6p2q+nmgFHgEbxqQESJytYh8OFXtdmGbo3az2tjduuXjq3Rud/ebtPme4/NiTS+loqaAOFBZU77LdRHpkI6b1QdV9WZV/TjenNHP4vW2duF5R+1mrby4xi6+KXZAoNvzYwuaX/rC0n2pqCsgNrsuIF3S8fj+Xar6lqpeo6rpngKklQVRN33rX/EV/aJM7+n+h+16em5RdP/TyawpQAJxWQZpDqIMsBlvtkiTgCmv6wsLNujxvT3OzMjVIbxe9qZ7NrkuIF0CFUSRikgcbykj04WCFo1edHMsX5IwH87AA9umDHhnq3Vy7L5nXBeQLoEKIp9dniXgx7fFVxa1JK8H/Mz1NaWoWs/27gnMJW0QgyjiuoBMd/Sm+NqZm3VB11smrrjp7eEjdz29JpnHzHH7gcA8cQxiEK1wXUAm6xPVd37wz/hQScF7o/SFpfPR2PZkHzdHPVNZUx6YwcNBDKLV2A3rTl20NLa2IJ6apbnz4819Jm3+V2CeBPVSoM4eAxdEkYpIM7DSdR2Z6OS18VWTdnJiKtuYsPWB4/NbGu2BQdcCdeYeuCDyPea6gEwz8KDu+cb/xiemuh0BmVZ3vU1Sd2gteKMRAsOCyADw6xtjm/KU4eloa9ie9bNKGvbY6PzOPVVZUx6oifyCGkRPArZMsu/TT8QfH7mPY9PZ5qzIVSNRtXnEO/ag6wLSLZBBFKmINAAPua4jEwzfp298flm8x0M4eqpf/Y7woH2brJNjxx5wXUC6BTKIfLe7LsA5Vb10SWyngJOFEWdsuG4mqjYo9v32AatcF5FuQQ6iu3A/UZtT//lgfHmonqNctV/YcnDw6DdW2Kof73dHZU154N6XgQ2iSEVkDwG+aT1+l77y0TU6z3UdU1/6x3G2MOP73OK6ABcCG0S+QF6e5cW15eKbYo0CfZzXorGiKS/dbr2tPbuBh10X4ULQg+gOIO66iHT77l3xx/s00eUk+Oky9o3Hji1oPrjOdR0Z4PbKmvIW10W4EOggilRE3gD+7bqOdDryVX3+2I16gus62pux4dp8W5gxmJdlEPAg8l3nuoB0KWrWhp/dGisRKHBdS3uD922aFvCFGV8mwPcsEwoiETlMRG4RkZdFZI2I3CsiU1NdXBc1dfmmFZFE5r+5C+/aPOf95O+x1YUxJrmuozOzIleHUW10XYcjVwdptH17XQaRiAjevZRHVXWyqs4BfgIdLzmcTCLS6W9u1d5PYQoQqYg0AX9OxrEy2fwX4s8euZWkzjGUbH0a94wZumd9EId+NAB/cV2ES4mcEZ0CNKvqu8tEq+paYIWIXC4i60UkIiJnAYjIySKyTETuEpFXRGSxiHxRRFb52032txsuIreLyGr/4wT/9WoRuUlEHgduEpGRInKHiKz1P473tzvg/9lfRB4SkWf843+yB9+HGnK4T1HfRt1/4R3xkeJ+XbkuTau7/ugALsx4c2VNeSBWdO1MIkE0nY7nRvkMMBuYBZwGXC4io/zPzQK+AZQB5wBTVXU+3v2Y8/1trgD+oKrzgM/y/ns1RwKnqerZwB+BZao6Czga2NCujkbg06p6NF5o/s4/i0tYpCLyKnBPd/bJJr/6a2x9vjLadR2JKIhFB4zf9lDQpgn5b9cFuNabm9UnAn9T1Ziq7gSWAa0d5Far6nZVjeLdhGsdOxMBwv7fTwOuFJHngLuBgSLS3//c3araOnlZOXA1gN/W/nZ1CHCpiKzDewI2hp5dNl7ag30y3oeeia8cv5uMe0p2KJNfueuEvFjzy67rSJPHKmvKn3VdhGuJBNEGSHypYV/bke3xNv+O894TmzzgWFWd7X+M0fcmVz/Yjba+CAwH5qjqbGAnUNLNeolURFYD93V3v0w26IDu/sr98Smu6+guQfNLX1walEuVX7kuIBMkEkQPA8Uicl7rCyIyE29w3lkiki8iw4GFdG+w3gO8d5mGiMzuZLuHgG/62+SLSPsBmiFgl6o2i8gpwIRu1NDef/Vi34xz6ZLY5jwY6rqOnjhs5+q5RU1v5/p0qcsra8ptFggSCCL1Opl9GjjNf3y/AfgNcDOwDliLF1Y/UtUd3Wj7O8BcEVknIs/j3VPqyHeBU0Qkgnevqn2P4KX+cSLAl4GN3ajhfSIVkZXkSAfHMx+LrRj2NvNd19EbMyM1A1DN5Z7vOfWLrzfEOrO+34wlM04ElruuozcO26vbrvif2CCBAa5r6a3Vc3684p0B41M6j7Yjyytryhe6LiJTWM/qdiIVkRXA/a7r6ClRjf96SWxvLoQQwMxIzdQcXZjxItcFZBILoo5dAGTlNKZfuy++fEAjs1zXkSzFTftHjNi1JtdWPL2nsqY8UJPjd8WCqAORishG4ErXdXTXpO266dTnNK1zT6dDWW4tzNgEfN91EZnGgqhz1XhdAbJCfkybq5fG4gLFrmtJtvx4U99Jm2tzpV/RFZU15ZvS0ZCIhEXkC+loq7csiDoRqYi8jTemLit87474EyXNHOG6jlSZsPX+E/Jj0Wzvcf0aCfQbSnCwdlfHyMfrsd1hF4j2ISUic0Xkj71tt6csiA7tBiDjB2HO2ByPzN2kufhk6V0CcuTzN2T7ElAXVtaUp+vG++HAZar6QiefDwPvBpGqPq2q30lHYR2xIDqESEVEgf+DN54tIxU36cGf/D0+UCDfdS2pNnzPutkljVm7MOPfK2vKb+vpziIyW0RW+v3u7hCRwf7r8/zXnmsdhO7vMgr4kb/NSf7nnxORZ0VkALAYWOC/dqE/WP1f/vb9ReR6fxD5OhH5rP/61SLytIhsEJGk9oGyIOpCpCLyPPAz13V05ue3xNYUxHvVmzyrzFx39YgsXJhxB/CtXh7jRuDHqjoTb8xm6+P/64Gv+8ObOptB4gdApb/NArxpR6qA5f7wqj+02/4XwH5VneG31zqP9s9UdS4wEzjJH2GRFBZEifkD8KjrIto7YUP86SNeJ1Cd4vrXb584aP9LT7quo5vOq6wp39PTnf1hTYNUdZn/0hJgoYgMAgaoauv34+ZODvE48HsR+Y5/nK7mxT6NNjMCqGrruL8zReQZ4FlgGh8c5dBjFkQJ8C/RzgXecVzKu/o36L5v3xMf67oOF6ZvuHY6H5yFIVMtqawpdzrFjKouBr6Kt2rL4yJS2t1jiMhEvDOrU/2zpFp6MLi8MxZECfLnLLrAdR2tLr4x9ny+cpjrOlwoaj44ZPT2x59zXUcCXsYbK9kr/tQ3b4lI6wyb5+DN0bUPeEdEjvFf/3xH+4vIZFWNqOplwGqgFO+Xame97x8EKtvsPxgYiDcrxn4RGQl8rJdf1vtYEHVDpCLyF+Am13X8x6r4E2P2kpSpcrPV1E1/P07iLVtd13EIDcBnKmvKe3Lm1ldEXmvz8T2gAm/ywXV4ExK2dgP4CnCtP69XP6Cj9i7wZ1Jdhzdi4H/xBqzH/FlPL2y3/SXAYH+ftcAp/qysz+INKr8Z73IvaWzQazfNWDKjBFhB9+doSoqhb+uOq/47Viww2EX7mWTbmJNWbppyZqb2JP9yZU15yn9piUj/1nm8RKQKGKWqvT4LSzc7I+qmSEWkEW9aFCfzKv96Sew1CyHPuNeXHVvQXJ+JCzNelY4Q8i3yH8Gvx3sidkma2k0qC6IeiFREtgGfA9K6KucXH4ktH3KAufimhzcAAAeCSURBVOlsM9NNz7yFGZ8kjfcSVfVW/xH8dFVdpKpZufCABVEPRSoiy4Dvpau9MW/qq59YqUenq71sMWTfi9P61u/MlMf5LwOfqqwpz7Z+Ts5ZEPVCpCLyJ7w+RimVF9fYJTfG3hbvZqRpZ1bk6vEZsDDjLuAjlTXluxzXkZUsiHrv+3hj0lLmm7XxFf2izEhlG9msT+ObY4fu3bDSYQkHgdMra8pzZYaAtLMg6iW/s+NXgTtTcfzDX9cXFq7X41Jx7Fwy7fnrj0bjbzpougU4o7KmfLWDtnOGBVESRCoiMbzOZA93tW13FLRo9KKbY3kCRck8bi4qiDUOHL/toefT3GwLcE5lTXlOLUPlggVRkkQqIlHgk3hPTZLih7fHVxa3kHXrkrky+ZW7TsiLp21hxmbg7Mqa8lvS1F5OsyBKokhF5ADwIbwu8r1y1EvxtbNf0QVdb2laCZp/xAt/25uGppqAM3szrYd5PwuiJItURA4CpwO39/QYJU164Ie3x4eI/f9026idT80rbHr7mRQ2EQU+W1lTnpJ7gkFlb/QUiFREmoCzgL/0ZP+LlsaeLYgzLrlVBcesSE3/FC3MuB9YVFlT/q8UHDvQLIhSJFIRiUUqIl8Bftud/U5eF181eQd2SdYLA995dWr/A68ldVAmsAU43paITg0LohSLVER+CJyHd1/hkAYe1D3fuDc+MfVV5T5/YcaDSTrcU8AxlTXl6X4qFxgWRGkQqYhcC5wMHHJtrktujG3KU4anpagcV9K0b+SI3c8ko2/P7cAp1mM6tSyI0iRSEXkSb+qQDh/vf/LJ+OOH7SNTp7TISmUb/zofjfd0YcYWvMnnP1dZU96QxLJMB2w+ojSbsWRGEd4qsl9rfW3Yft3+31fF+gqE3FWWmzZP+Ojjmyd+/IRu7rYNOKuypjxTBtPmPAsiR2YsmXEWUINq6Jo/xp4dVI+NrE8BBV224PcvxPOLE52n+V9ARWVNeTr6IxmfXZo5EqmI3ArMPOfh+J8thFJHQKbV3ZDIpVU9cCHwCQuh9LMzIsfqSssEOB/4DdDXcTk56/FjL14VLRkyv5NPPwJ8zUbPu2NBlCHqSssOx1tL6sOua8lFB/qN3rxq7k/HIVLQ5uW38ZbIua6yptx+EByyIMowdaVlnwZ+j7c2uUmiNbMvXLZ/0OEn+f+8Azi/sqb8dZc1GY8FUQaqKy3rg/fo+Md4i+KZJGgq7L/n8eMu3ah5+b+orCl/xHU95j0WRBmsrrQsDFyKN27NHiz0zmvAL4ElZRvrUjEOzfSCBVEWqCstK8P7IToTC6Tu2oF3qXtl2cY665iYoSyIsogFUre8AlwO3FC2sc71xPqmCxZEWaiutOwIvLXJK/DWJDfvWQcsBv5etrEu5roYkxgLoixWV1rWD/gS8C1gpuNyXGoAbgOuK9tY95jrYkz3WRDliLrSshOBrwCfAgY5Lidd1gB/Bm4u21i333UxpucsiHJMXWlZEV6nyDPxJvPPtUu3tXhLN/2zbGNdJq57b3rAgiiH1ZWWFQMfAf4DOBU43G1FPRIDluOFz11lG+u2uC3HpIIFUYDUlZZNAMrxQqkcGOW2og41AKuAFXgB9GTZxrq33ZZkUs2CKMDqSsvGArPbfUwCJE0l7AXqgOeBDXgBtKZsY12X0+qa3GJBZN6nrrRsAN44t/HtPsYBQ/AmbwvhzRSQ38EhmvHm524C3sLrUNj+42Xg+bKNdTtS+KWYLGJBZHqsrrSsEG8sXBxosjMZ01MWRMYY52yYgDHGOQsiY4xzFkRpJCIxEXmuzUdYRJ7IgLp+JSKnua7DBJfdI0ojETmgqv1d15EoEclXVRs4alLOzogcE5ED/p8ni8ijInKbiGwUkaUiIv7nfikiq0VkvYhc0+b1R0XkMhFZJSIvisgC//V8Efmtv/06ETnff32OiCwTkTUicr+IjPJfv0FEzvD/vsU/5jPA50TkbBGJ+Me6zMG3yASABVF69WlzWXZHB58/CrgAOBKvY2HrwoBXquo8VZ2O97j89Db7FKjqfH+/i/zXzsPrCzRbVWcCS0WkEPgTcIaqzgH+Avy6kzr3qOrRwGPAZXi9sGcD80TkUz35wo05lIKuNzFJ1KCqsw/x+VWq+hqAiDyHFyYrgFNE5Ed4nQiH4PVCvsff55/+n2t4b8L904AaVW0BUNW9IjIdmA486J9Q5QOdLcd8q//nPOBRVd3t17QUWIg37suYpLEgyizRNn+PAQUiUgJcBcxV1W0iUg2UdLBPjEP/fwqwQVWPS6COg4mXbEzv2aVZ5msNnTdFpD9wRgL7PAh8Xfw1vERkCPACMFxEjvNfKxSRaV0cZxVwkogME5F84GxgWU++CGMOxYIow6nqPuBaYD1wP7A6gd2uA7YC60RkLfAFVW3CC7HL/NeeA47vou3tQBXeSqhrgTWqeldPvxZjOmOP740xztkZkTHGOQsiY4xzFkTGGOcsiIwxzlkQGWOcsyAyxjhnQWSMcc6CyBjjnAWRMcY5CyJjjHMWRMYY5yyIjDHOWRAZY5yzIDLGOGdBZIxxzoLIGOPc/weut3Qlw0UzIAAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 350
        },
        "id": "2VFT9bsiR2jn",
        "outputId": "198187bf-f0d3-4c7e-f426-55b77d5dca34"
      },
      "source": [
        "\n",
        "employeeplot_df = employee_df['Area'].value_counts()\n",
        "\n",
        "employeeplot_df.plot(kind='pie')\n",
        "\n",
        "print(employee_df['Area'].value_counts())"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Comercial         26\n",
            "Administrativo    26\n",
            "Operações         23\n",
            "Logística         21\n",
            "Financeiro        18\n",
            "Name: Area, dtype: int64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XgYy7oT4UynY",
        "outputId": "cf562a11-42a6-45d4-ae66-2da880405572"
      },
      "source": [
        "meanservice = services_df['Valor Contrato Mensal'].mean()\n",
        "print(f'R$ {meanservice:,.2f}')"
      ],
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "R$ 2,438.35\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}