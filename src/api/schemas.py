from pydantic import BaseModel, Field, model_validator

class VehicleFeatures(BaseModel):
    brand: str
    model: str

    top_speed_kmh: float = Field(..., ge=60, le=350)
    battery_capacity_kWh: float = Field(..., ge=10, le=200)
    battery_type: str
    number_of_cells: int = Field(..., ge=50, le=9000)
    torque_nm: float = Field(..., ge=50, le=1200)
    efficiency_wh_per_km: float = Field(..., ge=80, le=300)
    acceleration_0_100_s: float = Field(..., ge=1.8, le=20)

    towing_capacity_kg: float = Field(..., ge=0, le=5000)
    cargo_volume_l: float = Field(..., ge=50, le=3000)
    seats: int = Field(..., ge=1, le=9)
    drivetrain: str
    segment: str

    length_mm: float = Field(..., ge=2500, le=6000)
    width_mm: float = Field(..., ge=1300, le=2500)
    height_mm: float = Field(..., ge=1200, le=2500)

    car_body_type: str
    source_url: str

    @model_validator(mode="after")
    def check_industry_ranges(cls, values):
        """Custom validation to report clean industry range errors."""

        # Define industry ranges clearly
        ranges = {
            "top_speed_kmh": (60, 350),
            "battery_capacity_kWh": (10, 200),
            "number_of_cells": (50, 9000),
            "torque_nm": (50, 1200),
            "efficiency_wh_per_km": (80, 300),
            "acceleration_0_100_s": (1.8, 20),
            "towing_capacity_kg": (0, 5000),
            "cargo_volume_l": (50, 3000),
            "seats": (1, 9),
            "length_mm": (2500, 6000),
            "width_mm": (1300, 2500),
            "height_mm": (1200, 2500),
        }

        errors = []

        for field, (min_val, max_val) in ranges.items():
            if field in values:
                val = values[field]
                if not (min_val <= val <= max_val):
                    errors.append(
                        f"{field}: {val} is outside the industry range [{min_val} – {max_val}]"
                    )

        if errors:
            raise ValueError({"industry_range_errors": errors})

        return values
