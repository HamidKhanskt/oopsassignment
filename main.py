def rifle_ak47(bullet_price: int, bullet_capacity: int):
    return {
        "bullet_price": bullet_price,
        "bullet_capacity": int(bullet_capacity)  
    }

def specification_gun(bullet_price, bullet_capacity, num_bullets):
    total_cost = bullet_price * num_bullets
    return total_cost

if __name__ == "__main__":
    
    capacity = input("Input capacity of magazine: ")
    
    
    ak47_spec = rifle_ak47(bullet_price=50, bullet_capacity=capacity)

    
    num_bullets = int(input("Enter number of bullets: "))  
    total_cost = specification_gun(bullet_price=ak47_spec["bullet_price"],
                                   bullet_capacity=ak47_spec["bullet_capacity"],
                                   num_bullets=num_bullets)
    
    print(f"Total cost for bullets: ${total_cost}")
