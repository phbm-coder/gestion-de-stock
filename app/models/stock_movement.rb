class StockMovement < ApplicationRecord
  VALID_TYPES = ['IN', 'OUT', 'ADJUSTMENT', 'RETURN'].freeze

  validates :quantity, presence: true, numericality: { greater_than: 0 }
  validates :movement_type, presence: true, inclusion: { in: VALID_TYPES }

  belongs_to :product
  belongs_to :user, optional: true

  scope :recent, -> { order(created_at: :desc) }
  scope :by_type, ->(type) { where(movement_type: type) }
  scope :by_date_range, ->(start_date, end_date) { where(created_at: start_date..end_date) }

  after_create :notify_if_critical

  private

  def notify_if_critical
    if product.low_stock?
      LowStockNotificationJob.perform_later(product.id)
    end
  end
end
