# Software-Engineering-URFU-2.7-Group
Project on the discipline of Software engineering group 27

## Молохов Д.А.
Модель:
[TAPEX: Table Pre-training via Learning a Neural SQL Executor](https://huggingface.co/microsoft/tapex-base-finetuned-wikisql).
Может быть использована для ответов на относительно простые вопросы по таблицам.

Был создан скрипт, принимающий на вход 2 аргумента: путь к csv-файлу и вопрос.

<details>
  <summary>Примеры использования:</summary>

### [Top 50 Spotify Songs - 2019](https://www.kaggle.com/datasets/leonardopena/top50spotify2019)

|   Unnamed: 0 | Track.Name                                    | Artist.Name        | Genre           |   Beats.Per.Minute |   Energy |   Danceability |   Loudness..dB.. |   Liveness |   Valence. |   Length. |   Acousticness.. |   Speechiness. |   Popularity |
|--------------:|:---------------------------------------------|:--------------------|:-----------------|-------------------:|----------:|--------------:|-----------------:|-----------:|-----------:|----------:|-----------------:|--------------:|------------:|
|            0 | Señorita                                     | Shawn Mendes        | canadian pop     |                117 |        55 |            76 |               -6 |          8 |         75 |       191 |                4 |             3 |          79 |
|            1 | China                                        | Anuel AA            | reggaeton flow   |                105 |        81 |            79 |               -4 |          8 |         61 |       302 |                8 |             9 |          92 |
|            2 | boyfriend (with Social House)               | Ariana Grande       | dance pop        |                190 |        80 |            40 |               -4 |         16 |         70 |       186 |               12 |            46 |          85 |
|            3 | Beautiful People (feat. Khalid)             | Ed Sheeran          | pop              |                 93 |        65 |            64 |               -8 |          8 |         55 |       198 |               12 |            19 |          86 |
|            4 | Goodbyes (Feat. Young Thug)                  | Post Malone         | dfw rap          |                150 |        65 |            58 |               -4 |         11 |         18 |       175 |               45 |             7 |          94 |
|            5 | I Don't Care (with Justin Bieber)            | Ed Sheeran          | pop              |                102 |        68 |            80 |               -5 |          9 |         84 |       220 |                9 |             4 |          84 |
|            6 | Ransom                                       | Lil Tecca           | trap music       |                180 |        64 |            75 |               -6 |          7 |         23 |       131 |                2 |            29 |          92 |
|            7 | How Do You Sleep?                            | Sam Smith           | pop              |                111 |        68 |            48 |               -5 |          8 |         35 |       202 |               15 |             9 |          90 |
|            8 | Old Town Road - Remix                        | Lil Nas X           | country rap      |                136 |        62 |            88 |               -6 |         11 |         64 |       157 |                5 |            10 |          87 |
|            9 | bad guy                                     | Billie Eilish       | electropop       |                135 |        43 |            70 |              -11 |         10 |         56 |       194 |               33 |            38 |          95 |
|           10 | Callaita                                    | Bad Bunny           | reggaeton        |                176 |        62 |            61 |               -5 |         24 |         24 |       251 |               60 |            31 |          93 |
|           11 | Loco Contigo (feat. J. Balvin & Tyga)        | DJ Snake            | dance pop        |                 96 |        71 |            82 |               -4 |         15 |         38 |       185 |               28 |             7 |          86 |
|           12 | Someone You Loved                           | Lewis Capaldi       | pop              |                110 |        41 |            50 |               -6 |         11 |         45 |       182 |               75 |             3 |          88 |
|           13 | Otro Trago - Remix                          | Sech                | panamanian pop   |                176 |        79 |            73 |               -2 |          6 |         76 |       288 |                7 |            20 |          87 |
|           14 | Money In The Grave (Drake ft. Rick Ross)    | Drake               | canadian hip hop |                101 |        50 |            83 |               -4 |         12 |         10 |       205 |               10 |             5 |          92 |
|           15 | No Guidance (feat. Drake)                   | Chris Brown         | dance pop        |                 93 |        45 |            70 |               -7 |         16 |         14 |       261 |               12 |            15 |          82 |
|           16 | LA CANCIÓN                                  | J Balvin            | latin            |                176 |        65 |            75 |               -6 |         11 |         43 |       243 |               15 |            32 |          90 |
|           17 | Sunflower - Spider-Man: Into the Spider-Verse | Post Malone         | dfw rap          |                 90 |        48 |            76 |               -6 |          7 |         91 |       158 |               56 |             5 |          91 |
|           18 | Lalala                                     | Y2K                | canadian hip hop |                130 |        39 |            84 |               -8 |         14 |         50 |       161 |               18 |             8 |          88 |
|           19 | Truth Hurts                                | Lizzo               | escape room      |                158 |        62 |            72 |               -3 |         12 |         41 |       173 |               11 |            11 |          91 |

```
python table.py spotify_top_50.csv "How many dance pop songs are there?"
# [' 3.0']

python table.py spotify_top_50.csv 'Who is the artist of a song named "Someone you loved"?'
# [' lewis capaldi']
```

### [Titanic Dataset](https://www.kaggle.com/datasets/brendan45774/test-file/)

|   PassengerId |   Survived |   Pclass | Name                                               | Sex    |   Age |   SibSp |   Parch | Ticket          |   Fare | Cabin   | Embarked   |
|--------------:|-----------:|---------:|:---------------------------------------------------|:-------|------:|--------:|--------:|:----------------|-------:|:--------|:-----------|
|           892 |          0 |        3 | Kelly, Mr. James                                  | male   |  34.5 |       0 |       0 | 330911          | 7.8292 | nan     | Q          |
|           893 |          1 |        3 | Wilkes, Mrs. James (Ellen Needs)                  | female |  47   |       1 |       0 | 363272          | 7     | nan     | S          |
|           894 |          0 |        2 | Myles, Mr. Thomas Francis                         | male   |  62   |       0 |       0 | 240276          | 9.6875 | nan     | Q          |
|           895 |          0 |        3 | Wirz, Mr. Albert                                  | male   |  27   |       0 |       0 | 315154          | 8.6625 | nan     | S          |
|           896 |          1 |        3 | Hirvonen, Mrs. Alexander (Helga E Lindqvist)     | female |  22   |       1 |       1 | 3101298         | 12.2875 | nan     | S          |
|           897 |          0 |        3 | Svensson, Mr. Johan Cervin                        | male   |  14   |       0 |       0 | 7538            | 9.225  | nan     | S          |
|           898 |          1 |        3 | Connolly, Miss. Kate                              | female |  30   |       0 |       0 | 330972          | 7.6292 | nan     | Q          |
|           899 |          0 |        2 | Caldwell, Mr. Albert Francis                     | male   |  26   |       1 |       1 | 248738          | 29     | nan     | S          |
|           900 |          1 |        3 | Abrahim, Mrs. Joseph (Sophie Halaut Easu)         | female |  18   |       0 |       0 | 2657            | 7.2292 | nan     | C          |
|           901 |          0 |        3 | Davies, Mr. John Samuel                           | male   |  21   |       2 |       0 | A/4 48871       | 24.15  | nan     | S          |
|           902 |          0 |        3 | Ilieff, Mr. Ylio                                  | male   |   0   |       0 |       0 | 349220          | 7.8958 | nan     | S          |
|           903 |          0 |        1 | Jones, Mr. Charles Cresson                        | male   |  46   |       0 |       0 | 694             | 26     | nan     | S          |
|           904 |          1 |        1 | Snyder, Mrs. John Pillsbury (Nelle Stevenson)    | female |  23   |       1 |       0 | 21228           | 82.2667 | B45    | S          |
|           905 |          0 |        2 | Howard, Mr. Benjamin                              | male   |  63   |       1 |       0 | 24065           | 26     | nan     | S          |
|           906 |          1 |        1 | Chaffee, Mrs. Herbert Fuller (Carrie Constance... | female |  47   |       1 |       0 | W.E.P. 5734     | 61.175  | E31    | S          |
|           907 |          1 |        2 | del Carlo, Mrs. Sebastiano (Argenia Genovesi)    | female |  24   |       1 |       0 | SC/PARIS 2167   | 27.7208 | nan     | C          |
|           908 |          0 |        2 | Keane, Mr. Daniel                                | male   |  35   |       0 |       0 | 233734          | 12.35  | nan     | Q          |
|           909 |          0 |        3 | Assaf, Mr. Gerios                                | male   |  21   |       0 |       0 | 2692            | 7.225  | nan     | C          |
|           910 |          1 |        3 | Ilmakangas, Miss. Ida Livija                     | female |  27   |       1 |       0 | STON/O2. 3101270 | 7.925  | nan     | S          |
|           911 |          1 |        3 | Assaf Khalil, Mrs. Mariana (Miriam")"            | female |  45   |       0 |       0 | 2696            | 7.225  | nan     | C          |

```
python table.py titanic.csv "What is the passengerid of Mr. Daniel Keane?"
# [' 908.0']

python table.py titanic.csv "What is the age of a person with the ticket '24065'?"
# [' 63.0']
```

</details>
