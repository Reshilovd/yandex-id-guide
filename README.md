# Инструкция: авторизация через Яндекс ID

Пошаговое руководство по созданию OAuth-приложения в кабинете Яндекс OAuth.

## Публикация на GitHub Pages

1. Создайте репозиторий на [GitHub](https://github.com/new) (например, `yandex-id-guide`).
2. В корне проекта выполните:

```powershell
git init
git add .
git commit -m "Публикация инструкции на GitHub Pages"
git branch -M main
git remote add origin https://github.com/ВАШ_ЛОГИН/yandex-id-guide.git
git push -u origin main
```

3. На GitHub откройте **Settings → Pages**:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/docs`
4. Сохраните. Через 1–3 минуты сайт будет доступен по адресу:

`https://ВАШ_ЛОГИН.github.io/ИМЯ_РЕПОЗИТОРИЯ/`

## Локальная проверка (необязательно)

Если установлен Ruby:

```powershell
cd docs
gem install bundler
bundle init
bundle add github-pages --group "jekyll_plugins"
bundle exec jekyll serve
```

Откройте http://localhost:4000/

## Структура

| Файл | Назначение |
|------|------------|
| `docs/index.md` | Текст инструкции |
| `docs/yandex-auth.css` | Стили |
| `docs/images/` | Скриншоты шагов |
| `docs/_layouts/default.html` | Шаблон страницы для Jekyll |
