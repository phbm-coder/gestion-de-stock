Rails.application.routes.draw do
  devise_for :users

  namespace :api do
    namespace :v1 do
      resources :products do
        get :low_stock, on: :collection
        resources :stock_movements, only: [:index, :create]
      end
      resources :stock_movements, only: [:index, :create]
      resources :categories
      resources :reports, only: [:index, :show]
    end
  end

  root "dashboard#index"
end
