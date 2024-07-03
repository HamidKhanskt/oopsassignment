class AK47:
    def __init__(self, bullet_price: int, bullet_capacity: int):
        self.bullet_price = bullet_price
        self.bullet_capacity = int(bullet_capacity)

    def specification_gun(self, num_bullets):
        total_cost = self.bullet_price * num_bullets
        return total_cost
30
if __name__ == "__main__":
    
    capacity = input("Input capacity of magazine: ")
    
    
    ak47 = AK47(bullet_price=50, bullet_capacity=capacity)

    
    num_bullets = int(input("Enter number of bullets: "))  
    total_cost = ak47.specification_gun(num_bullets)
    
    print(f"Total cost for bullets: ${total_cost}")
