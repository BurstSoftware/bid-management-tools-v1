# utils/scoring.py
def calculate_score(bid, bids, weights={
    "cost": 0.4, "timeline": 0.3, "experience": 0.2, "material_quality": 0.05, "warranty": 0.05
}):
    max_cost = max([b["cost"] for b in bids]) if bids else 1
    max_timeline = max([b["timeline"] for b in bids]) if bids else 1
    max_experience = max([b["experience"] for b in bids]) if bids else 1
    max_warranty = max([b["warranty"] for b in bids]) if bids else 1
    
    # Normalize scores (lower cost/timeline is better, higher experience/warranty/material is better)
    cost_score = (1 - bid["cost"] / max_cost) * 100
    timeline_score = (1 - bid["timeline"] / max_timeline) * 100
    experience_score = (bid["experience"] / max_experience) * 100
    warranty_score = (bid["warranty"] / max_warranty) * 100
    material_quality_score = bid["material_quality"] * 20  # Scale 1-5 to 0-100
    
    # Weighted score
    score = (
        weights["cost"] * cost_score +
        weights["timeline"] * timeline_score +
        weights["experience"] * experience_score +
        weights["material_quality"] * material_quality_score +
        weights["warranty"] * warranty_score
    )
    return round(score, 2)
