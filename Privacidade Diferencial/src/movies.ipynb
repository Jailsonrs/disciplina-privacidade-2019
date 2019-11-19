{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "library(data.table)\n",
    "library(dplyr)\n",
    "library(ggplot2)\n",
    "library(\"bit64\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "'/home/jrs/Área de Trabalho/disciplina-privacidade-2019/data/raw'"
      ],
      "text/latex": [
       "'/home/jrs/Área de Trabalho/disciplina-privacidade-2019/data/raw'"
      ],
      "text/markdown": [
       "'/home/jrs/Área de Trabalho/disciplina-privacidade-2019/data/raw'"
      ],
      "text/plain": [
       "[1] \"/home/jrs/Área de Trabalho/disciplina-privacidade-2019/data/raw\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<caption>A data.table: 6 × 28</caption>\n",
       "<thead>\n",
       "\t<tr><th scope=col>color</th><th scope=col>director_name</th><th scope=col>num_critic_for_reviews</th><th scope=col>duration</th><th scope=col>director_facebook_likes</th><th scope=col>actor_3_facebook_likes</th><th scope=col>actor_2_name</th><th scope=col>actor_1_facebook_likes</th><th scope=col>gross</th><th scope=col>genres</th><th scope=col>⋯</th><th scope=col>num_user_for_reviews</th><th scope=col>language</th><th scope=col>country</th><th scope=col>content_rating</th><th scope=col>budget</th><th scope=col>title_year</th><th scope=col>actor_2_facebook_likes</th><th scope=col>imdb_score</th><th scope=col>aspect_ratio</th><th scope=col>movie_facebook_likes</th></tr>\n",
       "\t<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>⋯</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;integr64&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th></tr>\n",
       "</thead>\n",
       "<tbody>\n",
       "\t<tr><td>Color</td><td>James Cameron    </td><td>723</td><td>178</td><td>    0</td><td>  855</td><td>Joel David Moore</td><td> 1000</td><td>760505847</td><td>Action|Adventure|Fantasy|Sci-Fi</td><td>⋯</td><td>3054</td><td>English</td><td>USA</td><td>PG-13</td><td>237000000</td><td>2009</td><td>  936</td><td>7.9</td><td>1.78</td><td> 33000</td></tr>\n",
       "\t<tr><td>Color</td><td>Gore Verbinski   </td><td>302</td><td>169</td><td>  563</td><td> 1000</td><td>Orlando Bloom   </td><td>40000</td><td>309404152</td><td>Action|Adventure|Fantasy       </td><td>⋯</td><td>1238</td><td>English</td><td>USA</td><td>PG-13</td><td>300000000</td><td>2007</td><td> 5000</td><td>7.1</td><td>2.35</td><td>     0</td></tr>\n",
       "\t<tr><td>Color</td><td>Sam Mendes       </td><td>602</td><td>148</td><td>    0</td><td>  161</td><td>Rory Kinnear    </td><td>11000</td><td>200074175</td><td>Action|Adventure|Thriller      </td><td>⋯</td><td> 994</td><td>English</td><td>UK </td><td>PG-13</td><td>245000000</td><td>2015</td><td>  393</td><td>6.8</td><td>2.35</td><td> 85000</td></tr>\n",
       "\t<tr><td>Color</td><td>Christopher Nolan</td><td>813</td><td>164</td><td>22000</td><td>23000</td><td>Christian Bale  </td><td>27000</td><td>448130642</td><td>Action|Thriller                </td><td>⋯</td><td>2701</td><td>English</td><td>USA</td><td>PG-13</td><td>250000000</td><td>2012</td><td>23000</td><td>8.5</td><td>2.35</td><td>164000</td></tr>\n",
       "\t<tr><td>     </td><td>Doug Walker      </td><td> NA</td><td> NA</td><td>  131</td><td>   NA</td><td>Rob Walker      </td><td>  131</td><td>       NA</td><td>Documentary                    </td><td>⋯</td><td>  NA</td><td>       </td><td>   </td><td>     </td><td>       NA</td><td>  NA</td><td>   12</td><td>7.1</td><td>  NA</td><td>     0</td></tr>\n",
       "\t<tr><td>Color</td><td>Andrew Stanton   </td><td>462</td><td>132</td><td>  475</td><td>  530</td><td>Samantha Morton </td><td>  640</td><td> 73058679</td><td>Action|Adventure|Sci-Fi        </td><td>⋯</td><td> 738</td><td>English</td><td>USA</td><td>PG-13</td><td>263700000</td><td>2012</td><td>  632</td><td>6.6</td><td>2.35</td><td> 24000</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "A data.table: 6 × 28\n",
       "\\begin{tabular}{r|llllllllllllllllllllllllllll}\n",
       " color & director\\_name & num\\_critic\\_for\\_reviews & duration & director\\_facebook\\_likes & actor\\_3\\_facebook\\_likes & actor\\_2\\_name & actor\\_1\\_facebook\\_likes & gross & genres & actor\\_1\\_name & movie\\_title & num\\_voted\\_users & cast\\_total\\_facebook\\_likes & actor\\_3\\_name & facenumber\\_in\\_poster & plot\\_keywords & movie\\_imdb\\_link & num\\_user\\_for\\_reviews & language & country & content\\_rating & budget & title\\_year & actor\\_2\\_facebook\\_likes & imdb\\_score & aspect\\_ratio & movie\\_facebook\\_likes\\\\\n",
       " <chr> & <chr> & <int> & <int> & <int> & <int> & <chr> & <int> & <int> & <chr> & <chr> & <chr> & <int> & <int> & <chr> & <int> & <chr> & <chr> & <int> & <chr> & <chr> & <chr> & <integr64> & <int> & <int> & <dbl> & <dbl> & <int>\\\\\n",
       "\\hline\n",
       "\t Color & James Cameron     & 723 & 178 &     0 &   855 & Joel David Moore &  1000 & 760505847 & Action\\textbar{}Adventure\\textbar{}Fantasy\\textbar{}Sci-Fi & CCH Pounder     & Avatar                                      &  886204 &   4834 & Wes Studi            & 0 & avatar\\textbar{}future\\textbar{}marine\\textbar{}native\\textbar{}paraplegic                           & http://www.imdb.com/title/tt0499549/?ref\\_=fn\\_tt\\_tt\\_1 & 3054 & English & USA & PG-13 & 237000000 & 2009 &   936 & 7.9 & 1.78 &  33000\\\\\n",
       "\t Color & Gore Verbinski    & 302 & 169 &   563 &  1000 & Orlando Bloom    & 40000 & 309404152 & Action\\textbar{}Adventure\\textbar{}Fantasy        & Johnny Depp     & Pirates of the Caribbean: At World's End    &  471220 &  48350 & Jack Davenport       & 0 & goddess\\textbar{}marriage ceremony\\textbar{}marriage proposal\\textbar{}pirate\\textbar{}singapore     & http://www.imdb.com/title/tt0449088/?ref\\_=fn\\_tt\\_tt\\_1 & 1238 & English & USA & PG-13 & 300000000 & 2007 &  5000 & 7.1 & 2.35 &      0\\\\\n",
       "\t Color & Sam Mendes        & 602 & 148 &     0 &   161 & Rory Kinnear     & 11000 & 200074175 & Action\\textbar{}Adventure\\textbar{}Thriller       & Christoph Waltz & Spectre                                     &  275868 &  11700 & Stephanie Sigman     & 1 & bomb\\textbar{}espionage\\textbar{}sequel\\textbar{}spy\\textbar{}terrorist                              & http://www.imdb.com/title/tt2379713/?ref\\_=fn\\_tt\\_tt\\_1 &  994 & English & UK  & PG-13 & 245000000 & 2015 &   393 & 6.8 & 2.35 &  85000\\\\\n",
       "\t Color & Christopher Nolan & 813 & 164 & 22000 & 23000 & Christian Bale   & 27000 & 448130642 & Action\\textbar{}Thriller                 & Tom Hardy       & The Dark Knight Rises                       & 1144337 & 106759 & Joseph Gordon-Levitt & 0 & deception\\textbar{}imprisonment\\textbar{}lawlessness\\textbar{}police officer\\textbar{}terrorist plot & http://www.imdb.com/title/tt1345836/?ref\\_=fn\\_tt\\_tt\\_1 & 2701 & English & USA & PG-13 & 250000000 & 2012 & 23000 & 8.5 & 2.35 & 164000\\\\\n",
       "\t       & Doug Walker       &  NA &  NA &   131 &    NA & Rob Walker       &   131 &        NA & Documentary                     & Doug Walker     & Star Wars: Episode VII - The Force Awakens  &       8 &    143 &                      & 0 &                                                                  & http://www.imdb.com/title/tt5289954/?ref\\_=fn\\_tt\\_tt\\_1 &   NA &         &     &       &        NA &   NA &    12 & 7.1 &   NA &      0\\\\\n",
       "\t Color & Andrew Stanton    & 462 & 132 &   475 &   530 & Samantha Morton  &   640 &  73058679 & Action\\textbar{}Adventure\\textbar{}Sci-Fi         & Daryl Sabara    & John Carter                                 &  212204 &   1873 & Polly Walker         & 1 & alien\\textbar{}american civil war\\textbar{}male nipple\\textbar{}mars\\textbar{}princess               & http://www.imdb.com/title/tt0401729/?ref\\_=fn\\_tt\\_tt\\_1 &  738 & English & USA & PG-13 & 263700000 & 2012 &   632 & 6.6 & 2.35 &  24000\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "A data.table: 6 × 28\n",
       "\n",
       "| color &lt;chr&gt; | director_name &lt;chr&gt; | num_critic_for_reviews &lt;int&gt; | duration &lt;int&gt; | director_facebook_likes &lt;int&gt; | actor_3_facebook_likes &lt;int&gt; | actor_2_name &lt;chr&gt; | actor_1_facebook_likes &lt;int&gt; | gross &lt;int&gt; | genres &lt;chr&gt; | ⋯ ⋯ | num_user_for_reviews &lt;int&gt; | language &lt;chr&gt; | country &lt;chr&gt; | content_rating &lt;chr&gt; | budget &lt;integr64&gt; | title_year &lt;int&gt; | actor_2_facebook_likes &lt;int&gt; | imdb_score &lt;dbl&gt; | aspect_ratio &lt;dbl&gt; | movie_facebook_likes &lt;int&gt; |\n",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
       "| Color | James Cameron     | 723 | 178 |     0 |   855 | Joel David Moore |  1000 | 760505847 | Action|Adventure|Fantasy|Sci-Fi | ⋯ | 3054 | English | USA | PG-13 | 237000000 | 2009 |   936 | 7.9 | 1.78 |  33000 |\n",
       "| Color | Gore Verbinski    | 302 | 169 |   563 |  1000 | Orlando Bloom    | 40000 | 309404152 | Action|Adventure|Fantasy        | ⋯ | 1238 | English | USA | PG-13 | 300000000 | 2007 |  5000 | 7.1 | 2.35 |      0 |\n",
       "| Color | Sam Mendes        | 602 | 148 |     0 |   161 | Rory Kinnear     | 11000 | 200074175 | Action|Adventure|Thriller       | ⋯ |  994 | English | UK  | PG-13 | 245000000 | 2015 |   393 | 6.8 | 2.35 |  85000 |\n",
       "| Color | Christopher Nolan | 813 | 164 | 22000 | 23000 | Christian Bale   | 27000 | 448130642 | Action|Thriller                 | ⋯ | 2701 | English | USA | PG-13 | 250000000 | 2012 | 23000 | 8.5 | 2.35 | 164000 |\n",
       "| <!----> | Doug Walker       |  NA |  NA |   131 |    NA | Rob Walker       |   131 |        NA | Documentary                     | ⋯ |   NA | <!----> | <!----> | <!----> |        NA |   NA |    12 | 7.1 |   NA |      0 |\n",
       "| Color | Andrew Stanton    | 462 | 132 |   475 |   530 | Samantha Morton  |   640 |  73058679 | Action|Adventure|Sci-Fi         | ⋯ |  738 | English | USA | PG-13 | 263700000 | 2012 |   632 | 6.6 | 2.35 |  24000 |\n",
       "\n"
      ],
      "text/plain": [
       "  color director_name     num_critic_for_reviews duration\n",
       "1 Color James Cameron     723                    178     \n",
       "2 Color Gore Verbinski    302                    169     \n",
       "3 Color Sam Mendes        602                    148     \n",
       "4 Color Christopher Nolan 813                    164     \n",
       "5       Doug Walker        NA                     NA     \n",
       "6 Color Andrew Stanton    462                    132     \n",
       "  director_facebook_likes actor_3_facebook_likes actor_2_name    \n",
       "1     0                     855                  Joel David Moore\n",
       "2   563                    1000                  Orlando Bloom   \n",
       "3     0                     161                  Rory Kinnear    \n",
       "4 22000                   23000                  Christian Bale  \n",
       "5   131                      NA                  Rob Walker      \n",
       "6   475                     530                  Samantha Morton \n",
       "  actor_1_facebook_likes gross     genres                          ⋯\n",
       "1  1000                  760505847 Action|Adventure|Fantasy|Sci-Fi ⋯\n",
       "2 40000                  309404152 Action|Adventure|Fantasy        ⋯\n",
       "3 11000                  200074175 Action|Adventure|Thriller       ⋯\n",
       "4 27000                  448130642 Action|Thriller                 ⋯\n",
       "5   131                         NA Documentary                     ⋯\n",
       "6   640                   73058679 Action|Adventure|Sci-Fi         ⋯\n",
       "  num_user_for_reviews language country content_rating budget    title_year\n",
       "1 3054                 English  USA     PG-13          237000000 2009      \n",
       "2 1238                 English  USA     PG-13          300000000 2007      \n",
       "3  994                 English  UK      PG-13          245000000 2015      \n",
       "4 2701                 English  USA     PG-13          250000000 2012      \n",
       "5   NA                                                        NA   NA      \n",
       "6  738                 English  USA     PG-13          263700000 2012      \n",
       "  actor_2_facebook_likes imdb_score aspect_ratio movie_facebook_likes\n",
       "1   936                  7.9        1.78          33000              \n",
       "2  5000                  7.1        2.35              0              \n",
       "3   393                  6.8        2.35          85000              \n",
       "4 23000                  8.5        2.35         164000              \n",
       "5    12                  7.1          NA              0              \n",
       "6   632                  6.6        2.35          24000              "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "getwd()\n",
    "movies <- data.table::fread(\"movie_metadata.csv\")\n",
    "movies %>% head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>4916</li>\n",
       "\t<li>28</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 4916\n",
       "\\item 28\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 4916\n",
       "2. 28\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] 4916   28"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "unique(movies, by = \"movie_title\") %>% dim()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R",
   "language": "R",
   "name": "ir"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
