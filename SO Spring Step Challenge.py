{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cadb9780-ff66-4997-9dae-574bebf4fa17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import random\n",
    "import os\n",
    "\n",
    "teams = {\n",
    "    \"Team 1\": {\"members\": [\"Ailidh Snook\", \"Ashleigh Wilcox\", \"Amber Vater\", \"Nicole Ashman\"], \"steps\": [], \"calories\": []},\n",
    "    \"Team 2\": {\"members\": [\"Becky Lyons-Helps\", \"Nikki Cholod\", \"Sian Giles-Titcombe\", \"Felcy Fernandes\", \"Maggie Wilson\"], \"steps\": [], \"calories\": []},\n",
    "    \"Team 3\": {\"members\": [\"Sarah Garlick\", \"Jane Long\", \"Mel Kidd\", \"Rachel Reynolds\"], \"steps\": [], \"calories\": []},\n",
    "}\n",
    "\n",
    "st.set_page_config(page_title=\"Step Challenge\", layout=\"wide\")\n",
    "\n",
    "challenge_image = \"images/step_challenge.jpg\"  \n",
    "if os.path.exists(challenge_image):\n",
    "    st.image(challenge_image, use_column_width=True)\n",
    "\n",
    "st.title(\"Step Challenge App - 1 Hour Fitness Challenge\")\n",
    "\n",
    "team_name = st.selectbox(\"Select Your Team\", list(teams.keys()))\n",
    "\n",
    "member_name = st.selectbox(\"Select Your Name\", teams[team_name][\"members\"])\n",
    "\n",
    "steps = st.number_input(\"Enter Steps Walked\", min_value=0, value=0, step=100)\n",
    "\n",
    "calories = steps * 0.04\n",
    "\n",
    "if st.button(\"Submit Data\"):\n",
    "    teams[team_name][\"steps\"].append(steps)\n",
    "    teams[team_name][\"calories\"].append(calories)\n",
    "    st.success(f\"{member_name} added {steps} steps and burned {calories:.2f} calories!\")\n",
    "\n",
    "st.header(f\" {team_name} - Statistics\")\n",
    "if teams[team_name][\"steps\"]:\n",
    "    df = pd.DataFrame({\"Steps\": teams[team_name][\"steps\"], \"Calories\": teams[team_name][\"calories\"]})\n",
    "    st.dataframe(df)\n",
    "\n",
    "    fig, ax = plt.subplots(1, 2, figsize=(12, 4))\n",
    "    \n",
    "    ax[0].plot(df[\"Steps\"], marker=\"o\", linestyle=\"-\", color=\"blue\", label=\"Steps\")\n",
    "    ax[0].set_title(\"Steps Progress\")\n",
    "    ax[0].set_ylabel(\"Steps\")\n",
    "    ax[0].legend()\n",
    "    \n",
    "    ax[1].plot(df[\"Calories\"], marker=\"o\", linestyle=\"-\", color=\"red\", label=\"Calories\")\n",
    "    ax[1].set_title(\"Calories Burned\")\n",
    "    ax[1].set_ylabel(\"Calories\")\n",
    "    ax[1].legend()\n",
    "    \n",
    "    st.pyplot(fig)\n",
    "\n",
    "motivational_quotes = [\n",
    "    \"Keep going! Every step counts! \",\n",
    "    \"You're doing great! Stay active! \",\n",
    "    \"One step at a time! Keep moving! \",\n",
    "]\n",
    "st.subheader(random.choice(motivational_quotes))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e526d03d-9ebc-4acb-ae31-7a34c3acb28e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "effd59a4-ed48-42d9-85f7-697e8767c671",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2c8d704-07d4-42a3-8980-d12a5177c26f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a2380a2-ef09-41e1-9041-04893b6f8ef9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66154a02-9112-444e-b3e6-3db7b39942be",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bf9434b-97c2-4697-a627-64d9e1dc4aec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3782b13-4a0e-4265-91c2-652eb187658d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
