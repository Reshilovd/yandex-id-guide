---
layout: default
title: Создание приложения для авторизации пользователей с помощью Яндекс ID
---

# Создание приложения для авторизации пользователей с помощью Яндекс ID

<div class="page">

<aside class="sidebar">

<p class="sidebar-title"><b>Содержание</b></p>

<a href="#step-1">Шаг 1. Кабинет Яндекс OAuth</a>
<a href="#step-2">Шаг 2. Создание приложения</a>
<a href="#step-3">Шаг 3. Верификация</a>
<a href="#step-4">Шаг 4. Сведения о приложении</a>
<a href="#step-5">Шаг 5. Redirect URI</a>
<a href="#step-6">Шаг 6. Доступ к данным</a>
<a href="#step-7">Шаг 7. Завершение регистрации</a>

</aside>

<main class="content">

<h2 id="step-1">Шаг 1. Перейти в кабинет Яндекс OAuth</h2>

Авторизуйтесь в сервисе [Яндекс OAuth](https://oauth.yandex.ru/) через аккаунт, с помощью которого планируете продолжать разработку.

<div class="two-column">

<img src="./images/step-1.png" alt="Кабинет Яндекс OAuth" width="260" class="step-image">

<div class="note warning text">

<h4>Важно</h4>

Чтобы не потерять доступ к приложению, используйте аккаунт, к которому у вас всегда будет доступ.

</div>


</div>

---

<h2 id="step-2">Шаг 2. Создать приложение</h2>

1. Нажмите кнопку <b>Создать</b>. 
2. Во всплывающем окне выберите <b>Для авторизации пользователей</b> 
3. Нажмите <b>Перейти к созданию</b>.

<div class="image-row">
  <img src="./images/step-2-1.png" alt="Создание приложения" height="250">
  <img src="./images/step-2-2.png" alt="Выбор типа приложения" height="250">
</div>

---

<h2 id="step-3">Шаг 3. Пройти верификацию (опционально)</h2>

Далее будет предложено пройти верификацию аккаунта. Она даёт следующие преимущества:

1. Доступ к технической поддержке Яндекс OAuth.
2. Возможность регистрации более 5 приложений.
3. Доступ к дополнительной информации о пользователе.

Подробнее об этом процессе можно прочитать в [документации](https://yandex.ru/dev/id/doc/ru/confirm-account). Это окно можно закрыть и продолжить создание приложения, либо пройти верификацию сразу.


<div class="image-row">
  <img src="./images/step-3-1.png" alt="Верификация аккаунта" height="300">
  <img src="./images/step-3-2.png" alt="Информация о верификации" height="300">
</div>

---

<h2 id="step-4">Шаг 4. Указать сведения о приложении</h2>

<div class="two-column">

<img src="./images/step-4.png" alt="Настройка сведений о приложении" class="step-image">

<div class="text">

1. Укажите <b>название сервиса</b>.
2. Загрузите <b>иконку</b> размером до 1 МБ.
3. Заполните поле <b>Почта для связи</b>. Убедитесь, что адрес актуален, чтобы не пропустить важную информацию об изменениях в продукте.
4. Нажмите <b>Продолжить</b>.

</div>

</div>

---

<h2 id="step-5">Шаг 5. Настроить платформу и Redirect URI</h2>

<div class="two-column">

<img src="./images/step-5.png" alt="Настройка Redirect URI" class="step-image">

<div class="text">

1. В списке платформ выберите <b>Веб-сервисы</b>.
2. Укажите <b>Redirect URI</b>.
3. Если используете несколько окружений, например `dev`, `stage` и `prod`, добавьте для них отдельные Redirect URI.
4. Поле <b>Suggest Hostname</b> можно оставить пустым.
5. Нажмите <b>Продолжить</b>.

</div>

</div>

<div class="note">

<h4>Примечание</h4>

`Redirect URI`, указанный в OAuth-приложении, может не полностью совпадать с URI в запросе, однако следующие части адреса должны совпадать:

Например, для адреса `https://example.ru:8443/oauth/callback?source=yandex#done`:

- схема: `https` — <span class="uri-match">должна совпадать</span>
- хост: `example.ru` — <span class="uri-match">должен совпадать</span>
- порт: `8443` — <span class="uri-match">должен совпадать</span>
- путь: `/oauth/callback` — <span class="uri-match">должен совпадать</span>
- запрос (`query`): `source=yandex` — <span class="uri-optional">может не совпадать</span>
- фрагмент (`fragment`): `done` — <span class="uri-optional">может не совпадать</span>

</div>

<h2 id="step-6">Шаг 6. Доступ к данным</h2>

<div class="two-column">

<img src="./images/step-6.png" alt="Настройка доступа к данным" class="step-image">

<div class="text">

1. Выберите данные пользователя, доступ к которым нужно получить.
2. Нажмите <b>Продолжить</b>.

</div>

</div>


<div class="note">

<h4>Основные и дополнительные данные</h4>

<p><b>Основные</b> — это базовые данные профиля, которые обычно нужны для авторизации пользователя:</p>

- дата рождения;
- адрес электронной почты;
- логин, имя, фамилия, пол;
- портрет пользователя;
- номер телефона.

<p><b>Дополнительные</b> — это расширенные права доступа к другим сервисам Яндекса, например к Диску, Директу и другим API.</p>

<p>Если вам нужна только авторизация пользователя, обычно достаточно основных данных. Запрашивайте только те права, которые действительно нужны вашему сервису.</p>

</div>

<details markdown="1">
<summary markdown="span"><strong>Полный список доступных данных и scopes</strong></summary>
<details markdown="1">
<summary>🔐 Базовые данные пользователя (Login API)</summary>
| Scope | Описание |
| --- | --- |
| `login:info` | Логин, имя, фамилия, пол |
| `login:email` | Email пользователя |
| `login:avatar` | Аватар пользователя |
| `login:birthday` | Дата рождения |
| `login:default_phone` | Номер телефона |
| `login:address.home_work.read` | Домашний и рабочий адрес |
| `login:address.all.read` | Все адреса пользователя |
| `login:promo_subscription` | Подписка на рекламные сообщения |
</details>
<details markdown="1">
<summary>☁️ Яндекс.Диск</summary>
| Scope | Описание |
| --- | --- |
| `cloud_api:disk.read` | Чтение всего Диска |
| `cloud_api:disk.write` | Запись на Диск |
| `cloud_api:disk.info` | Информация о Диске |
| `cloud_api:disk.app_folder` | Доступ к папке приложения |
| `yadisk:disk` | Полный доступ к API Яндекс.Диска |
</details>
<details markdown="1">
<summary>✉️ Почта</summary>
| Scope | Описание |
| --- | --- |
| `mail:imap_ro` | Чтение почты |
| `mail:imap_full` | Чтение и удаление писем |
| `mail:smtp` | Отправка почты через SMTP |
</details>
<details markdown="1">
<summary>📊 Метрика / AppMetrica / Audience</summary>
| Scope | Описание |
| --- | --- |
| `metrika:read` | Чтение статистики Метрики |
| `metrika:write` | Изменение счётчиков |
| `metrika:user_params` | Загрузка параметров пользователей |
| `metrika:expenses` | Загрузка расходов |
| `metrika:segments` | Управление сегментами |
| `metrika:offline_data` | Загрузка офлайн-данных |
| `appmetrica:read` | Чтение AppMetrica |
| `appmetrica:write` | Управление AppMetrica |
| `audience:read` | Чтение сегментов |
| `audience:write` | Управление сегментами |
</details>
<details markdown="1">
<summary>🌐 Вебмастер / SEO</summary>
| Scope | Описание |
| --- | --- |
| `webmaster:hostinfo` | Внешние ссылки сайта |
| `webmaster:verify` | Подтверждение сайта |
| `webmaster:turbopages` | Турбо-страницы |
| `wordstat:api` | API Wordstat |
| `suggest:read_web_history` | История поисковых запросов |
</details>
<details markdown="1">
<summary>📅 Календарь / Контакты / Коммуникации</summary>
| Scope | Описание |
| --- | --- |
| `calendar:all` | Полный доступ к календарю |
| `addressbook:all` | Адресная книга |
| `yamb:all` | Чаты Яндекса |
| `messenger:vconf` | Конференции Messenger |
| `telemost-api:conferences.read` | Чтение встреч Телемоста |
| `telemost-api:conferences.create` | Создание встреч |
| `telemost-api:conferences.update` | Изменение встреч |
| `telemost-api:conferences.delete` | Удаление встреч |
</details>
<details markdown="1">
<summary>🏢 Яндекс 360 / Организации</summary>
| Scope | Описание |
| --- | --- |
| `directory:read_users` | Чтение сотрудников |
| `directory:write_users` | Управление сотрудниками |
| `directory:read_groups` | Чтение групп |
| `directory:write_groups` | Управление группами |
| `directory:read_departments` | Чтение подразделений |
| `directory:write_departments` | Управление подразделениями |
| `directory:read_domains` | Чтение доменов |
| `directory:write_domains` | Управление доменами |
| `directory:manage_dns` | Управление DNS |
| `directory:read_organization` | Чтение организации |
| `directory:write_organization` | Редактирование организации |
</details>
<details markdown="1">
<summary>🛡️ Безопасность Яндекс 360</summary>
| Scope | Описание |
| --- | --- |
| `ya360_security:read_auditlog` | Чтение аудит-лога |
| `ya360_security:audit_log_mail` | Аудит лог почты |
| `ya360_security:audit_log_disk` | Аудит лог диска |
| `ya360_security:domain_2fa_write` | Управление 2FA |
| `ya360_security:domain_passwords_read` | Чтение настроек паролей |
| `ya360_security:domain_passwords_write` | Управление паролями |
| `ya360_security:domain_sessions_read` | Чтение сессий |
| `ya360_security:domain_sessions_write` | Управление сессиями |
| `ya360_security:domain_settings_read` | Чтение настроек безопасности |
| `ya360_security:domain_settings_write` | Изменение настроек безопасности |
</details>
<details markdown="1">
<summary>📬 Администрирование почты Яндекс 360</summary>
| Scope | Описание |
| --- | --- |
| `ya360_admin:mail_read_user_settings` | Чтение настроек почты |
| `ya360_admin:mail_write_user_settings` | Изменение настроек почты |
| `ya360_admin:mail_read_routing_rules` | Чтение routing rules |
| `ya360_admin:mail_write_routing_rules` | Изменение routing rules |
| `ya360_admin:mail_read_domain_routes` | Чтение маршрутизации |
| `ya360_admin:mail_write_domain_routes` | Управление маршрутизацией |
| `ya360_admin:mail_read_antispam_settings` | Чтение антиспама |
| `ya360_admin:mail_write_antispam_settings` | Управление антиспамом |
</details>
<details markdown="1">
<summary>💳 Финансы / Оплата</summary>
| Scope | Описание |
| --- | --- |
| `yandexpay:all` | Оплата через Yandex Pay |
| `yandexpay:merchant-api` | Управление заказами |
| `split:api` | Оплата частями |
</details>
<details markdown="1">
<summary>🚚 Доставка / Логистика</summary>
| Scope | Описание |
| --- | --- |
| `delivery:partner-api` | API Яндекс.Доставки |
| `courier:logistician` | Курьеры и заказы |
</details>
<details markdown="1">
<summary>🤖 IoT / Умный дом</summary>
| Scope | Описание |
| --- | --- |
| `iot:view` | Просмотр устройств |
| `iot:control` | Управление устройствами |
</details>
<details markdown="1">
<summary>📚 Wiki / Tracker / Forms</summary>
| Scope | Описание |
| --- | --- |
| `wiki:read` | Чтение Wiki |
| `wiki:write` | Запись в Wiki |
| `tracker:read` | Чтение Tracker |
| `tracker:write` | Запись в Tracker |
| `forms:read` | Просмотр форм |
| `forms:write` | Управление формами |
</details>
<details markdown="1">
<summary>📢 Реклама / Маркетинг / Ads</summary>
| Scope | Описание |
| --- | --- |
| `direct:api` | API Яндекс.Директа |
| `adfox:api` | API Adfox |
| `promopages:api` | API ПромоСтраниц |
| `partner_office:api` | API партнёрского кабинета |
| `partner_office:advmarkup` | Маркировка рекламы |
| `market:partner-api` | API Яндекс.Маркета |
| `products:partner-api` | Поиск товаров |
</details>
<details markdown="1">
<summary>🧠 AI / Нейросети</summary>
| Scope | Описание |
| --- | --- |
| `masterpiecer:all` | API Шедеврум |
| `neuro-expert:all` | Нейроэксперт |
</details>
<details markdown="1">
<summary>🚴 Прочее</summary>
| Scope | Описание |
| --- | --- |
| `maps:public_bookmarks` | Закладки карт |
| `scooters:write` | Самокаты |
| `chargers:write` | Зарядки |
| `tv:use` | Телепрограмма |
| `cid:use` | Яндекс.АОН |
| `cloud:auth` | Аутентификация в Облаке |
</details>
</details>

<h2 id="step-7">Шаг 7. Завершение регистрации</h2>

<div class="two-column">

<img src="./images/step-7.png" alt="Завершение регистрации" class="step-image">

<div class="text">

После настройки всех параметров приложения в Яндекс OAuth отобразится окно, которое увидят пользователи, когда войдут в приложение с помощью Яндекс ID. Чтобы подтвердить сохранение, нажмите <b>Всё верно</b>.

</div>

</div>
</main>

</div>
