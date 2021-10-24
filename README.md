# Acceleration-consortium-hackaton

Repository for the hackaton at Acceleration Consortium '21

### Team
- **Name: DFQI-FCEN-UBA**
- **Team members:**
    - Diego Onna
    - Guillermo Fiorini
    - Juan Santiago Grassano
    - María Belén Ticona


## Proyect description

Our aim is to facilitate the preparation of colloidal nanoparticles by creating an open SQL dataset on the experimental conditions. In particular, for this challenge we will focus on the synthesis of silica nanoparticles. These particles are widely used in industrial applications, medicine and science. To give an example, last year the global silica nanoparticles market was $3.2 billion and around 72k research papers involving silica nanoparticles have been published. We aim to integrate visualization tools for the data and develop machine learning and statistical models that could predict particle sizes and their dispersion from the experimental conditions. Anyone interested in synthesizing silica particles could make use of these tools to optimize their experimental parameters in order to reach a certain particle diameter in a quick, simple way, without the need of previous coding knowledge. It can also be used by data scientists interested in developing new models and statistical studies on the topic. Opening the dataset may not only provide the opportunity for entirely new studies and discoveries, but may also encourage researchers to add new instances based on their own experimental data and push the materials science community to create open datasets on other materials, making access to reproducible synthesis information easier for anyone interested and advancing the nanosynthesis field in a more sustainable way globally.

## "Good" goal

Our first goal for this Sunday is to create, using Molar, a SQL dataset on silica synthesis conditions. To do that, we will restrict the scope to the Stöber method, which provides calibrated and monodisperse silica particles, is robust and scalable. We will design the DB according to the available bibliographical information on the subject and extract the experimental conditions from relevant articles and design the dataset based on them.

Our second goal is to design a simple workflow for scientists without coding skills to upload new instances to the dataset, with their experimental data and perform queries to the database.

## "Better" goal

If we had a full week to continue working, we would implement libraries and tools to make statistical analysis and visualization of the data. We could also develop a better user interface to allow the input of new instances and the visualization in a more friendly environment. With this, we aim at building a community of contributors of new synthesis data to enrich the dataset that will allow better models for Stöber synthesis to be studied.

## "Best" goal

If we had a month to continue coding, we would expand our SQL database to include other synthesis methods and experimental conditions and, also, implement others machine learning models to predict silica nanoparticles diameter from the experimental conditions. This will facilitate new synthesis for the community, as it will allow to automatically search the optimal experimental conditions to reach the desired particle size that has not been synthesized before.
We would also aim to improve the dataset so it can be used to enter data on other material synthesis conditions, other properties and characterization results (e.g. UV-VIS spectra). Our long-term vision is that the nanosynthesis research community opens and shares its data as this will advance the nanosynthesis field in a more reproducible and sustainable way globally.


## Requirements

- Python 3.7.4
- `pipenv`
- Molar


## Installation

Run the following commands in a terminal in the current repository:

1. Clone the repository
2. `pipenv sync`
3. ``python -m ipykernel install --user --name=acceleration-consortium-hackaton`

Now it is possible to edit the Jupyter Notebook selecting the project environment.

If you prefer to run the script by console, open a shell in the environment with the following command: `pipenv shell`

## Usage

1. Check port 5432 is available. If it is not, find processes that are using it and kill them.

2. Run: `molarcli install local`

   - Full Name: admin
   - Mail ticona.belu@gmail.com 

3. Create an alembic revision 

   `cd molar`

   `molarcli alembic revision -m "revision_name" --branch-label "revision_name" --head f31 --splice`
   
## Data searching and selection

All experimental data were retrieved from already published works, theses and laboratory notebooks. The searching for articles was made using the searching engine of _Dimensions_.

We selected works that studied the influence of the reaction parameters on the final particle diameter while following Stöber’s classical synthesis protocol. Ideally, conducting a multivariable assessment study, following a factorial synthesis design.

Having selected the papers and works, their data was collected manually from their tables, results sections, and plots.

The dataset follows the FAIR principles to make it findable, accessible, interoperable, and reusable, making it public and available for any person that is interested in the study of this synthesis. We also aim at building a community of contributors of new synthesis data to enrich the dataset that will allow better models for Stöber synthesis to be studied.

## Raw data

The database consists of a total of 732 Stöber syntheses as reported in 35 publications and it has been presented in CSV format.

Columns of the csv dataset: 
* TEOS concentration 
* Alcohol concentration
* Ammonia concentration
* Water concentration
* NaCl concentration
* Agitation
* Temperature
* Time
* Mixture volume
* Mixture mass
* Mixture mass error
* Container volume
* Aggregate speed
* Size
* Standard deviation
* Polydispersity
* Measurement technique
* Concentration Units
* Alcohol
* Year
* Reference


## SQL Dataset design

- Designed a relational data base schema using PosgresSQL by Molar interface: "Stober DB"
- Modeled the problem with 10 tables, populating the data for one of them as a example. Tables:
- Planned data mapping between raw data and the "Stober DB" data base.

#### Stöber Data Base Diagram

![Stöber Data Base Diagram](https://raw.githubusercontent.com/pacasi/acceleration-consortium-hackaton/main/img/stober_db_diagram.png)

![code](https://raw.githubusercontent.com/pacasi/acceleration-consortium-hackaton/main/img/data_entries_molar_examples.png)


![code2](https://raw.githubusercontent.com/pacasi/acceleration-consortium-hackaton/main/img/molar_view_db.png)

### GUI

![GUI Plot](https://raw.githubusercontent.com/pacasi/acceleration-consortium-hackaton/main/img/GUI%20plot.png)


![GUI Submit](https://raw.githubusercontent.com/pacasi/acceleration-consortium-hackaton/main/img/GUI%20submit.png=350x)

## Future works and improvements

With the SQL dataset created using Molar, the next step is to link it to the graphic interface of the csv dataset and prepare a user interface to allow the input of new instances and the visualization in a more friendly environment. After that, with time we hope to reach the "best" goals previously mentioned.
