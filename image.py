from google.adk.tools.tool_context import ToolContext
from IPython.display import display, Image as IPImage
import base64
from uuid import UUID

# TODO how get mcp to pass this image to this function?

def request(num_images: int, request_id: UUID , tool_context: ToolContext) -> dict[int, IPImage]:
    """
    Requests a sample image to be generated. Requires approval
    if the number of images requested is more than 1.

    Args:
        num_images: Number of images requested
        request_id: Unique ID labeling the request
    Returns:
        Dictionary with the image
    """

    # 1 image requested: auto-approve
    if num_images <= 1:
        return {
            "status": "approved",
            "request_id": request_id,
            "num_images": num_images,
            "image": "IMAGE",
            "message": f"Auto-approved: {num_images} image"
        }

    # *First* time tool is called - and needs human approval - pause here.
    if not tool_context.tool_confirmation:
        tool_context.request_confirmation(
            hint=f"Large request: {num_images} images. Do you want to approve?",
            payload={"num_images": num_images, "request_id":request_id}
        )
        return { # sent to agent
            "status": "pending",
            "message": f"Request for {num_images} images requires approval",
        }

    pass