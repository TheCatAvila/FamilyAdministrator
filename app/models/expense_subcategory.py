from app.database.db_connection import Database

class ExpenseSubcategory:
    def __init__(self, id: int = None, name: str = None, budget: str = None, category_id: int = None):
        self.id = id
        self.name = name
        self.budget = budget
        self.category_id = category_id
    
    def get_all(self):
        """Obtiene todas las subcategorías de egresos."""
        try:
            query = "SELECT * FROM expense_subcategory"
            with Database() as db:
                db.execute(query)
                subcategories = db.fetchall()
            
            return {"success": True, "subcategories": subcategories}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def get_total_budget_by_family(self, family_id: int):
        """Obtiene el total del presupuesto de todas las subcategorías."""
        try:
            query = """SELECT 
                            SUM(es.budget) AS total_family_budget
                        FROM 
                            expense_category ec
                        LEFT JOIN 
                            expense_subcategory es ON ec.id = es.category_id
                        WHERE 
                            ec.family_id = %s;""" 
            with Database() as db:
                values = (family_id,)
                db.execute(query, values)
                total_budget = db.fetchone()
            
            return {"success": True, "total_budget": total_budget['total_family_budget']}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def get_by_category_id(self):
        """Obtiene todas las subcategorías de egresos por categoría."""
        try:
            query = "SELECT * FROM expense_subcategory WHERE category_id = %s"
            values = (self.category_id,)
            
            with Database() as db:
                db.execute(query, values)
                subcategories = db.fetchall()
            
            return {"success": True, "subcategories": subcategories}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}

    def create(self):
        """Crea una nueva subcategoría de egresos."""
        try:
            query = "INSERT INTO expense_subcategory (name, budget, category_id) VALUES (%s, %s, %s)"
            values = (self.name, self.budget, self.category_id)
            print("Valores a insertar: ", values)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Subcategoría creada exitosamente."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def delete(self):
        """Elimina una subcategoría de egresos."""
        try:
            query = "DELETE FROM expense_subcategory WHERE id = %s"
            values = (self.id,)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Subcategoría eliminada exitosamente."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}