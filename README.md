## Описание проекта

В этом проекте была натренирована модель классификации с использованием алгоритма RandomForestClassifier. Модель предназначена для решения задачи классификации и была подготовлена для развертывания в контейнере.

## Этапы работы

1. **Обучение модели**:
   - Модель RandomForestClassifier была успешно натренирована на наборе данных.
   - Результаты обучения были сохранены в файле формата joblib для дальнейшего использования.

2. **Создание контейнера**:
   - Контейнер был создан с использованием Docker. В Dockerfile были указаны все необходимые зависимости и команды для запуска приложения.

3. **Публикация в Docker репозиторий**:
   - Контейнер был загружен (push) в Docker репозиторий, что позволяет легко делиться и развертывать модель в различных окружениях.

4. **Запуск через Minikube**:
   - Контейнер был развернут в Kubernetes с использованием Minikube, что обеспечило удобное управление кластером и возможность масштабирования приложения.

## Структура проекта

- `model.joblib` — файл с сохраненной моделью RandomForestClassifier.
- `Dockerfile` — файл с инструкциями для создания Docker-образа.
- `docker-compose.yml` — файл для управления многоуровневыми приложениями с использованием Docker.

## Установка и запуск

1. Убедитесь, что у вас установлены Docker и Minikube.
2. Склонируйте репозиторий:
   ```
   git clone <URL_репозитория>
   ```
3. Запустите Minikube:
   ```
   minikube start
   ```
4. Постройте и запустите контейнер:
   ```
   docker build -t <имя_образа> .
   docker run <имя_образа>
   ```
5. Разверните приложение в Minikube:
   ```
   kubectl apply -f deployment.yaml
   ```
## Полезные команды
```
minikube start (stop)
minikube status
kubectl create namespace <name>
kubectl apply -f deployment.yaml -n <name space>
kubectl apply -f service.yaml -n <name space>
kubectl get pods -n <name space>
kubectl describe pod <name pod> -n <name space>
kubectl get service -n <name space>
kubectl get secret
kubectl delete pod <pod name> -n <name space>
kubectl delete deployment <deployment_name>
kubectl delete secrets --all
kubectl logs <pod name> -n <name space>
```
### Проброс секретов
```
kubectl create secret docker-registry regcred \
2    --docker-server=YOUR_DOCKER_SERVER (https://index.docker.io/v1/) \
3    --docker-username=YOUR_USERNAME \
4    --docker-password=YOUR_PASSWORD \
5    --docker-email=YOUR_EMAIL \
6    -n your-namespace
```
```
docker build -t
docker tag
docker push
```
## Ошибки, с которыми я столкнулся:
### Не полный requirements.txt, решение, как я понял это
### ``` kubectl logs <pod name> -n <name space> ```
