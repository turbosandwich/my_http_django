Отдача статических файлов

/home/box
home/box/web/
home/box/web/public
home/box/web/public/img
home/box/web/public/css
home/box/web/public/js
home/box/web/uploads
home/box/web/etc

Префикс - /uploads/ в директорию /home/web/updloads

Суффикс - *.*(с расширением) отдавались из директории home/box/web/public

Суффикс - без расширения - Ошибка HTTP 404

Фрагмент конфига nginx:
 /home/box/web/etc/nginx.conf 
включен в основной конфиг с помощью символической ссылки.

nginx принимает запросы на порту 80 и обслуживает любые домены.

