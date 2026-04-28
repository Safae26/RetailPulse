# RetailPulse Inventory Optimization — ROP/EOQ calculator + simulation

import numpy as np
from pathlib import Path
from scipy.stats import norm
import json

class InventoryOptimization:
    """
    ROP/EOQ calculator with interactive parameters.
    """
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent.parent
        self.models_dir = self.base_dir / 'models'
        self.saved_strategy = None
        self._load_data()

    def _load_data(self):
        """Load saved inventory strategy."""
        p = self.models_dir / 'inventory_strategy.json'
        if p.exists():
            with open(p) as f:
                self.saved_strategy = json.load(f)

    # ── Calculator ────────────────────────────────────
    def calculate(self, lead_time=2, service_level=0.95, ordering_cost=500,
                  holding_cost=0.5, avg_demand=10000, std_demand=2000):
        """Calculate Safety Stock, ROP, EOQ."""
        z = norm.ppf(service_level)
        safety_stock = z * np.sqrt(lead_time) * std_demand
        reorder_point = avg_demand * lead_time + safety_stock
        annual_demand = avg_demand * 52
        eoq = np.sqrt((2 * annual_demand * ordering_cost) / (holding_cost * 52))
        annual_orders = annual_demand / eoq
        total_cost = (annual_orders * ordering_cost) + ((eoq / 2) * holding_cost * 52)

        return {
            'safety_stock': round(safety_stock, 0),
            'reorder_point': round(reorder_point, 0),
            'eoq': round(eoq, 0),
            'annual_orders': round(annual_orders, 1),
            'total_cost': round(total_cost, 0),
            'z_score': round(z, 3),
        }

    # ── Simulation ────────────────────────────────────
    def simulate(self, lead_time=2, reorder_point=30000, safety_stock=15000,
                 eoq=15000, avg_demand=10000, std_demand=2000, weeks=12):
        """Run a 12-week inventory simulation."""
        np.random.seed(42)
        stock = reorder_point + eoq / 2
        inventory = [stock]
        orders = []

        pending = []
        for week in range(1, weeks + 1):
            for arr_week, qty in pending[:]:
                if arr_week == week:
                    stock += qty
                    pending.remove((arr_week, qty))

            demand = avg_demand + np.random.normal(0, std_demand * 0.1)
            stock -= demand
            inventory.append(max(0, stock))

            total_pos = stock + sum(q for _, q in pending)
            if total_pos <= reorder_point:
                pending.append((week + lead_time, int(eoq)))
                orders.append(week)

        return {
            'inventory': [round(v, 0) for v in inventory],
            'order_weeks': orders,
            'reorder_point': round(reorder_point, 0),
            'safety_stock': round(safety_stock, 0),
            'stockouts': sum(1 for v in inventory if v == 0),
        }

    def get_saved_strategy(self):
        """Return the saved baseline strategy from the notebook."""
        return self.saved_strategy