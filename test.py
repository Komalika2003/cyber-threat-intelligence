try:
    import flask
    import sklearn
    import pandas as pd
    import crecs
    print("✅ ALL LIBRARIES INSTALLED CORRECTLY!")
    print(f"Flask: {flask.__version__}")
    print(f"scikit-learn: {sklearn.__version__}")
except ImportError as e:
    print(f"❌ ERROR: {e}")
