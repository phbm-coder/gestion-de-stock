class Api::V1::ProductsController < ApplicationController
  before_action :set_product, only: [:show, :update, :destroy]
  before_action :authenticate_user!
  before_action :authorize_user!

  def index
    @products = Product.includes(:category)
    @products = @products.by_category(params[:category_id]) if params[:category_id]
    @products = @products.search(params[:search]) if params[:search]
    @products = @products.page(params[:page]).per(20)

    render json: @products, each_serializer: ProductSerializer
  end

  def show
    render json: @product, serializer: ProductDetailSerializer
  end

  def create
    @product = Product.new(product_params)

    if @product.save
      render json: @product, serializer: ProductSerializer, status: :created
    else
      render json: { errors: @product.errors.full_messages }, status: :unprocessable_entity
    end
  end

  def update
    if @product.update(product_params)
      render json: @product, serializer: ProductSerializer
    else
      render json: { errors: @product.errors.full_messages }, status: :unprocessable_entity
    end
  end

  def destroy
    @product.destroy
    head :no_content
  end

  def low_stock
    @products = Product.low_stock
    render json: @products, each_serializer: ProductSerializer
  end

  private

  def set_product
    @product = Product.find(params[:id])
  end

  def product_params
    params.require(:product).permit(:name, :barcode, :price, :quantity, :min_quantity, :category_id, :description)
  end

  def authorize_user!
    authorize @product if @product
  end
end
