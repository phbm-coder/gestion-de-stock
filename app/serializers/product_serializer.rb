class ProductSerializer < ActiveModel::Serializer
  attributes :id, :name, :barcode, :price, :quantity, :min_quantity, :category_id, :description, :created_at, :updated_at, :low_stock

  def low_stock
    object.low_stock?
  end
end
