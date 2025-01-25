using Microsoft.AspNetCore.Mvc;
using Microsoft.FeatureManagement;

namespace YourProjectName.Controllers  // Add your project's namespace here
{
    public class HomeController : Controller
    {
        private readonly IFeatureManager _featureManager;

        public HomeController(IFeatureManager featureManager)
        {
            _featureManager = featureManager;
        }

        public async Task<IActionResult> Index()
        {
            string featureAMessage = "FeatureA is disabled!";
            string featureBMessage = "FeatureB is disabled!";

            // Check if FeatureA is enabled
            if (await _featureManager.IsEnabledAsync("FeatureA"))
            {
                featureAMessage = "FeatureA is enabled!";
            }

            // Check if FeatureB is enabled
            if (await _featureManager.IsEnabledAsync("FeatureB"))
            {
                featureBMessage = "FeatureB is enabled!";
            }

            // Set the messages in ViewData
            ViewData["FeatureAMessage"] = featureAMessage;
            ViewData["FeatureBMessage"] = featureBMessage;

            return View();
        }
    }
}
