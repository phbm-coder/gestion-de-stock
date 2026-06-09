# Backend - Gestion de Stocks (Ruby/Rails)

## 💎 Framework Web Rapide avec Rails

Backend Ruby on Rails pour développement agile avec excellentes relations modèles.

## 🚀 Installation

```bash
git clone https://github.com/phbm-coder/gestion-de-stock.git
cd gestion-de-stock
git checkout dev/backend-ruby

bundle install
rails db:create
rails db:migrate
rails server
```

## 📁 Structure

```
app/
├── models/
│   ├── product.rb
│   ├── stock_movement.rb
│   └── user.rb
├── controllers/
│   └── api/v1/
│       ├── products_controller.rb
│       └── stock_movements_controller.rb
├── serializers/
│   ├── product_serializer.rb
│   └── stock_movement_serializer.rb
config/
├── routes.rb
└── database.yml
```

## 🎯 Fonctionnalités

- ✅ API RESTful rapide
- ✅ Authentification Devise
- ✅ Autorisation Pundit
- ✅ Sérialisation ActiveModel
- ✅ Recherche Ransack
- ✅ Pagination Kaminari
- ✅ Jobs Sidekiq

## 🛠️ Technologies

- Ruby 3.2
- Rails 7.0
- PostgreSQL 14+
- Devise (Auth)
- Pundit (Authorization)
- Sidekiq (Background jobs)
- Redis (Cache & Jobs)

## 📦 Commands

```bash
# Migrations
rails db:migrate

# Tests
rails test

# Server
rails server

# Sidekiq
bundle exec sidekiq
```
