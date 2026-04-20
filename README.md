# BD Project — CI/CD

Автоматический деплой на VPS при пуше в `main`.

## Стек

- **Сервер:** Ubuntu 22.04 (Selectel)
- **CI/CD:** GitHub Actions
- **Доступ:** SSH-ключ, пользователь `dev`

## Как работает

`git push origin main` → GitHub Actions подключается по SSH → `git pull` в `/var/www/bd`

## Секреты GitHub

| Secret | Назначение |
| :--- | :--- |
| `SSH_HOST` | IP сервера |
| `SSH_USER` | `dev` |
| `SSH_PRIVATE_KEY` | Приватный SSH-ключ |

## Статус

- [x] Сервер + Git
- [x] CI/CD (deploy.yml)
- [x] Пользователь `dev`
- [ ] Docker-сборка
- [ ] Код приложения
