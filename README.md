## Marketplace Connector

App for managing marketplace

#### License

MIT

#### how to manual sync

di dalam sync_method e tanggale di ganti dulu semua ke tanggal mau di sync manual baru execute dibawah ini

bench --site pollapollyv12.antzman.com execute marketplace_connector.marketplace_connector.doctype.sync_method.enqueue_up_to_order_management_manual_1_500 --kwargs '{"date":"2021-04-06"}'

bench --site pollapollyv12.antzman.com execute marketplace_connector.marketplace_connector.doctype.sync_method.enqueue_up_to_order_management_manual_500_900 --kwargs '{"date":"2021-04-06"}'

bench --site pollapollyv12.antzman.com execute marketplace_connector.marketplace_connector.doctype.sync_method.enqueue_up_to_order_management_manual_900_1300 --kwargs '{"date":"2021-04-06"}'

bench --site pollapollyv12.antzman.com execute marketplace_connector.marketplace_connector.doctype.sync_method.enqueue_up_to_order_management_manual_1300_1700 --kwargs '{"date":"2021-04-06"}'

bench --site pollapollyv12.antzman.com execute marketplace_connector.marketplace_connector.doctype.sync_method.enqueue_up_to_order_management_manual_1700_2100 --kwargs '{"date":"2021-04-06"}'

bench --site pollapollyv12.antzman.com execute marketplace_connector.marketplace_connector.doctype.sync_method.enqueue_up_to_order_management_manual_2100_2500 --kwargs '{"date":"2021-04-06"}'