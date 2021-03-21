# datamining_curse

**Запуск даггера**

1. `pip install apache-airflow`

2. `export AIRFLOW_HOME=~/airflow/`

3. `airflow db init`

4. `airflow users create —username admin —e admin@ex.ru -f admin -l admin -r Admin`

5. `airflow webserver -p 5000`

6. `создаем папку dags в airflow`

7. `копируем airflow_dagger.py в папку dags`

8. `airflow schedule` - чтобы ипортнулся наш даггер в airflow

**Допольнительный материал**

`https://khashtamov.com/ru/apache-airflow-introduction/`
