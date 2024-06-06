from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def sign_up_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if password == confirm_password:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                login(request, user)
                return redirect("dashboard")
            else:
                form.add_error("password", "Password did not match")
        else:
            form = SignUpForm()
        context = {
            "forrm": form,
        }
        # enter reactjs file here
        return render(request, "authentication/...", context)
