using Microsoft.FeatureManagement;

var builder = WebApplication.CreateBuilder(args);

// Add Feature Management services
builder.Services.AddFeatureManagement();

// Add other services to the container
builder.Services.AddRazorPages();

var app = builder.Build();

// Configure the HTTP request pipeline
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
