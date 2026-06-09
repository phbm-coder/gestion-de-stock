class Product < ApplicationRecord
  validates :name, :barcode, :price, presence: true
  validates :barcode, uniqueness: true
  validates :price, numericality: { greater_than_or_equal_to: 0 }
  validates :quantity, :min_quantity, numericality: { only_integer: true }

  belongs_to :category, optional: true
  has_many :stock_movements, dependent: :destroy
  has_many :images, as: :imageable, dependent: :destroy

  scope :low_stock, -> { where("quantity <= min_quantity") }
  scope :by_category, ->(category_id) { where(category_id: category_id) }
  scope :search, ->(term) { where("name ILIKE ? OR barcode ILIKE ?", "%#{term}%", "%#{term}%") }

  def low_stock?
    quantity <= min_quantity
  end

  def record_movement(quantity, movement_type, reason = nil, user_id = nil)
    stock_movements.create!(
      quantity: quantity,
      movement_type: movement_type,
      reason: reason,
      user_id: user_id
    )

    case movement_type
    when 'IN', 'RETURN'
      increment!(:quantity, by: quantity)
    when 'OUT', 'ADJUSTMENT'
      decrement!(:quantity, by: quantity)
    end
  end
end
