{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "file = \"Resources/sampleData.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
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
       "      <th>id</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>Phone Number</th>\n",
       "      <th>Time zone</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Peter</td>\n",
       "      <td>Richardson</td>\n",
       "      <td>7-(789)867-9023</td>\n",
       "      <td>Europe/Moscow</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Janice</td>\n",
       "      <td>Berry</td>\n",
       "      <td>86-(614)973-1727</td>\n",
       "      <td>Asia/Harbin</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Andrea</td>\n",
       "      <td>Hudson</td>\n",
       "      <td>86-(918)527-6371</td>\n",
       "      <td>Asia/Shanghai</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Arthur</td>\n",
       "      <td>Mcdonald</td>\n",
       "      <td>420-(553)779-7783</td>\n",
       "      <td>Europe/Prague</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Kathy</td>\n",
       "      <td>Morales</td>\n",
       "      <td>351-(720)541-2124</td>\n",
       "      <td>Europe/Lisbon</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id first_name   last_name       Phone Number      Time zone\n",
       "0   1      Peter  Richardson    7-(789)867-9023  Europe/Moscow\n",
       "1   2     Janice       Berry   86-(614)973-1727    Asia/Harbin\n",
       "2   3     Andrea      Hudson   86-(918)527-6371  Asia/Shanghai\n",
       "3   4     Arthur    Mcdonald  420-(553)779-7783  Europe/Prague\n",
       "4   5      Kathy     Morales  351-(720)541-2124  Europe/Lisbon"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_original = pd.read_csv(file)\n",
    "df_original.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
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
       "      <th>id</th>\n",
       "      <th>first_name</th>\n",
       "      <th>Phone Number</th>\n",
       "      <th>Time zone</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>last_name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Richardson</th>\n",
       "      <td>1</td>\n",
       "      <td>Peter</td>\n",
       "      <td>7-(789)867-9023</td>\n",
       "      <td>Europe/Moscow</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Berry</th>\n",
       "      <td>2</td>\n",
       "      <td>Janice</td>\n",
       "      <td>86-(614)973-1727</td>\n",
       "      <td>Asia/Harbin</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Hudson</th>\n",
       "      <td>3</td>\n",
       "      <td>Andrea</td>\n",
       "      <td>86-(918)527-6371</td>\n",
       "      <td>Asia/Shanghai</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mcdonald</th>\n",
       "      <td>4</td>\n",
       "      <td>Arthur</td>\n",
       "      <td>420-(553)779-7783</td>\n",
       "      <td>Europe/Prague</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Morales</th>\n",
       "      <td>5</td>\n",
       "      <td>Kathy</td>\n",
       "      <td>351-(720)541-2124</td>\n",
       "      <td>Europe/Lisbon</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            id first_name       Phone Number      Time zone\n",
       "last_name                                                  \n",
       "Richardson   1      Peter    7-(789)867-9023  Europe/Moscow\n",
       "Berry        2     Janice   86-(614)973-1727    Asia/Harbin\n",
       "Hudson       3     Andrea   86-(918)527-6371  Asia/Shanghai\n",
       "Mcdonald     4     Arthur  420-(553)779-7783  Europe/Prague\n",
       "Morales      5      Kathy  351-(720)541-2124  Europe/Lisbon"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Set new index to last_name\n",
    "df = df_original.set_index(\"last_name\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using Loc: 86-(614)973-1727\n",
      "Using Iloc: 86-(614)973-1727\n"
     ]
    }
   ],
   "source": [
    "# Grab the data contained within the \"Berry\" row and the \"Phone Number\" column\n",
    "berry_phone = df.loc[\"Berry\", \"Phone Number\"]\n",
    "print(\"Using Loc: \" + berry_phone)\n",
    "\n",
    "also_berry_phone = df.iloc[1, 2]\n",
    "print(\"Using Iloc: \" + also_berry_phone)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            id first_name       Phone Number\n",
      "last_name                                   \n",
      "Richardson   1      Peter    7-(789)867-9023\n",
      "Richardson  25     Donald   62-(259)282-5871\n",
      "Berry        2     Janice   86-(614)973-1727\n",
      "Hudson       3     Andrea   86-(918)527-6371\n",
      "Hudson       8    Frances   57-(752)864-4744\n",
      "Hudson      90      Norma  351-(551)598-1822\n",
      "Mcdonald     4     Arthur  420-(553)779-7783\n",
      "Morales      5      Kathy  351-(720)541-2124\n",
      "\n",
      "            id first_name       Phone Number\n",
      "last_name                                   \n",
      "Richardson   1      Peter    7-(789)867-9023\n",
      "Berry        2     Janice   86-(614)973-1727\n",
      "Hudson       3     Andrea   86-(918)527-6371\n",
      "Mcdonald     4     Arthur  420-(553)779-7783\n"
     ]
    }
   ],
   "source": [
    "# Grab the first five rows of data and the columns from \"id\" to \"Phone Number\"\n",
    "# The problem with using \"last_name\" as the index is that the values are not unique so duplicates are returned\n",
    "# If there are duplicates and loc[] is being used, Pandas will return an error\n",
    "richardson_to_morales = df.loc[[\"Richardson\", \"Berry\", \"Hudson\",\n",
    "                                \"Mcdonald\", \"Morales\"], [\"id\", \"first_name\", \"Phone Number\"]]\n",
    "print(richardson_to_morales)\n",
    "\n",
    "print()\n",
    "\n",
    "# Using iloc[] will not find duplicates since a numeric index is always unique\n",
    "also_richardson_to_morales = df.iloc[0:4, 0:3]\n",
    "print(also_richardson_to_morales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
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
       "      <th>first_name</th>\n",
       "      <th>Phone Number</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>last_name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Richardson</th>\n",
       "      <td>Peter</td>\n",
       "      <td>7-(789)867-9023</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Berry</th>\n",
       "      <td>Janice</td>\n",
       "      <td>86-(614)973-1727</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Hudson</th>\n",
       "      <td>Andrea</td>\n",
       "      <td>86-(918)527-6371</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mcdonald</th>\n",
       "      <td>Arthur</td>\n",
       "      <td>420-(553)779-7783</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Morales</th>\n",
       "      <td>Kathy</td>\n",
       "      <td>351-(720)541-2124</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           first_name       Phone Number\n",
       "last_name                               \n",
       "Richardson      Peter    7-(789)867-9023\n",
       "Berry          Janice   86-(614)973-1727\n",
       "Hudson         Andrea   86-(918)527-6371\n",
       "Mcdonald       Arthur  420-(553)779-7783\n",
       "Morales         Kathy  351-(720)541-2124"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# The following will select all rows for columns `first_name` and `Phone Number`\n",
    "df.loc[:, [\"first_name\", \"Phone Number\"]].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "last_name\n",
       "Richardson    False\n",
       "Berry         False\n",
       "Hudson        False\n",
       "Mcdonald      False\n",
       "Morales       False\n",
       "Name: first_name, dtype: bool"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# the following logic test/conditional statement returns a series of boolean values\n",
    "named_billy = df[\"first_name\"] == \"Billy\"\n",
    "named_billy.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           id first_name      Phone Number       Time zone\n",
      "last_name                                                 \n",
      "Clark      20      Billy  62-(213)345-2549   Asia/Makassar\n",
      "Andrews    23      Billy  86-(859)746-5367  Asia/Chongqing\n",
      "Price      59      Billy  86-(878)547-7739   Asia/Shanghai\n",
      "\n",
      "            id first_name      Phone Number       Time zone\n",
      "last_name                                                  \n",
      "Richardson   1      Peter   7-(789)867-9023   Europe/Moscow\n",
      "Clark       20      Billy  62-(213)345-2549   Asia/Makassar\n",
      "Andrews     23      Billy  86-(859)746-5367  Asia/Chongqing\n",
      "Price       59      Billy  86-(878)547-7739   Asia/Shanghai\n"
     ]
    }
   ],
   "source": [
    "# Loc and Iloc also allow for conditional statments to filter rows of data\n",
    "# using Loc on the logic test above only returns rows where the result is True\n",
    "only_billys = df.loc[df[\"first_name\"] == \"Billy\", :]\n",
    "print(only_billys)\n",
    "\n",
    "print()\n",
    "\n",
    "# Multiple conditions can be set to narrow down or widen the filter\n",
    "only_billy_and_peter = df.loc[(df[\"first_name\"] == \"Billy\") | (\n",
    "    df[\"first_name\"] == \"Peter\"), :]\n",
    "print(only_billy_and_peter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
