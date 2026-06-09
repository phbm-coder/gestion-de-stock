source "https://rubygems.org"
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

ruby "3.2.0"

gem "rails", "~> 7.0.0"
gem "pg", "~> 1.5"
gem "puma", "~> 5.0"
gem "sass-rails", ">= 6"
gem "webpacker", "~> 5.0"
gem "devise"
gem "pundit"
gem "active_model_serializers"
gem "kaminari"
gem "ransack"
gem "sidekiq"
gem "redis", "~> 4.0"
gem "aws-sdk-s3", require: false
gem "stripe"

group :development, :test do
  gem "byebug", platforms: [:mri, :mingw, :x64_mingw]
  gem "rspec-rails"
  gem "factory_bot_rails"
end

group :development do
  gem "web-console", ">= 4.1.0"
  gem "rubocop", require: false
end
