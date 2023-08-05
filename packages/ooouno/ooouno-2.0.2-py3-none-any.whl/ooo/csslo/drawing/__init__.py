# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
warnings.filterwarnings('module')
warnings.warn('The csslo namespace is deprecated. Use lo instead.', DeprecationWarning, stacklevel=2)
from ...lo.drawing.accessible_draw_document_view import AccessibleDrawDocumentView as AccessibleDrawDocumentView
from ...lo.drawing.accessible_graph_control import AccessibleGraphControl as AccessibleGraphControl
from ...lo.drawing.accessible_graphic_shape import AccessibleGraphicShape as AccessibleGraphicShape
from ...lo.drawing.accessible_image_bullet import AccessibleImageBullet as AccessibleImageBullet
from ...lo.drawing.accessible_ole_shape import AccessibleOLEShape as AccessibleOLEShape
from ...lo.drawing.accessible_shape import AccessibleShape as AccessibleShape
from ...lo.drawing.accessible_slide_view import AccessibleSlideView as AccessibleSlideView
from ...lo.drawing.accessible_slide_view_object import AccessibleSlideViewObject as AccessibleSlideViewObject
from ...lo.drawing.alignment import Alignment as Alignment
from ...lo.drawing.applet_shape import AppletShape as AppletShape
from ...lo.drawing.arrangement import Arrangement as Arrangement
from ...lo.drawing.background import Background as Background
from ...lo.drawing.bar_code import BarCode as BarCode
from ...lo.drawing.bar_code_error_correction import BarCodeErrorCorrection as BarCodeErrorCorrection
from ...lo.drawing.bezier_point import BezierPoint as BezierPoint
from ...lo.drawing.bitmap_mode import BitmapMode as BitmapMode
from ...lo.drawing.bitmap_table import BitmapTable as BitmapTable
from ...lo.drawing.bound_volume import BoundVolume as BoundVolume
from ...lo.drawing.camera_geometry import CameraGeometry as CameraGeometry
from ...lo.drawing.caption_escape_direction import CaptionEscapeDirection as CaptionEscapeDirection
from ...lo.drawing.caption_shape import CaptionShape as CaptionShape
from ...lo.drawing.caption_type import CaptionType as CaptionType
from ...lo.drawing.circle_kind import CircleKind as CircleKind
from ...lo.drawing.closed_bezier_shape import ClosedBezierShape as ClosedBezierShape
from ...lo.drawing.color_mode import ColorMode as ColorMode
from ...lo.drawing.color_table import ColorTable as ColorTable
from ...lo.drawing.connection_type import ConnectionType as ConnectionType
from ...lo.drawing.connector_properties import ConnectorProperties as ConnectorProperties
from ...lo.drawing.connector_shape import ConnectorShape as ConnectorShape
from ...lo.drawing.connector_type import ConnectorType as ConnectorType
from ...lo.drawing.control_shape import ControlShape as ControlShape
from ...lo.drawing.coordinate_sequence import CoordinateSequence as CoordinateSequence
from ...lo.drawing.coordinate_sequence_sequence import CoordinateSequenceSequence as CoordinateSequenceSequence
from ...lo.drawing.custom_shape import CustomShape as CustomShape
from ...lo.drawing.custom_shape_engine import CustomShapeEngine as CustomShapeEngine
from ...lo.drawing.dash_style import DashStyle as DashStyle
from ...lo.drawing.dash_table import DashTable as DashTable
from ...lo.drawing.defaults import Defaults as Defaults
from ...lo.drawing.direction3_d import Direction3D as Direction3D
from ...lo.drawing.document_settings import DocumentSettings as DocumentSettings
from ...lo.drawing.double_sequence import DoubleSequence as DoubleSequence
from ...lo.drawing.double_sequence_sequence import DoubleSequenceSequence as DoubleSequenceSequence
from ...lo.drawing.draw_page import DrawPage as DrawPage
from ...lo.drawing.draw_pages import DrawPages as DrawPages
from ...lo.drawing.draw_view_mode import DrawViewMode as DrawViewMode
from ...lo.drawing.drawing_document import DrawingDocument as DrawingDocument
from ...lo.drawing.drawing_document_draw_view import DrawingDocumentDrawView as DrawingDocumentDrawView
from ...lo.drawing.drawing_document_factory import DrawingDocumentFactory as DrawingDocumentFactory
from ...lo.drawing.ellipse_shape import EllipseShape as EllipseShape
from ...lo.drawing.enhanced_custom_shape_adjustment_value import EnhancedCustomShapeAdjustmentValue as EnhancedCustomShapeAdjustmentValue
from ...lo.drawing.enhanced_custom_shape_extrusion import EnhancedCustomShapeExtrusion as EnhancedCustomShapeExtrusion
from ...lo.drawing.enhanced_custom_shape_geometry import EnhancedCustomShapeGeometry as EnhancedCustomShapeGeometry
from ...lo.drawing.enhanced_custom_shape_glue_point_type import EnhancedCustomShapeGluePointType as EnhancedCustomShapeGluePointType
from ...lo.drawing.enhanced_custom_shape_handle import EnhancedCustomShapeHandle as EnhancedCustomShapeHandle
from ...lo.drawing.enhanced_custom_shape_metal_type import EnhancedCustomShapeMetalType as EnhancedCustomShapeMetalType
from ...lo.drawing.enhanced_custom_shape_parameter import EnhancedCustomShapeParameter as EnhancedCustomShapeParameter
from ...lo.drawing.enhanced_custom_shape_parameter_pair import EnhancedCustomShapeParameterPair as EnhancedCustomShapeParameterPair
from ...lo.drawing.enhanced_custom_shape_parameter_type import EnhancedCustomShapeParameterType as EnhancedCustomShapeParameterType
from ...lo.drawing.enhanced_custom_shape_path import EnhancedCustomShapePath as EnhancedCustomShapePath
from ...lo.drawing.enhanced_custom_shape_segment import EnhancedCustomShapeSegment as EnhancedCustomShapeSegment
from ...lo.drawing.enhanced_custom_shape_segment_command import EnhancedCustomShapeSegmentCommand as EnhancedCustomShapeSegmentCommand
from ...lo.drawing.enhanced_custom_shape_text_frame import EnhancedCustomShapeTextFrame as EnhancedCustomShapeTextFrame
from ...lo.drawing.enhanced_custom_shape_text_path import EnhancedCustomShapeTextPath as EnhancedCustomShapeTextPath
from ...lo.drawing.enhanced_custom_shape_text_path_mode import EnhancedCustomShapeTextPathMode as EnhancedCustomShapeTextPathMode
from ...lo.drawing.escape_direction import EscapeDirection as EscapeDirection
from ...lo.drawing.fill_properties import FillProperties as FillProperties
from ...lo.drawing.fill_style import FillStyle as FillStyle
from ...lo.drawing.flag_sequence import FlagSequence as FlagSequence
from ...lo.drawing.flag_sequence_sequence import FlagSequenceSequence as FlagSequenceSequence
from ...lo.drawing.generic_draw_page import GenericDrawPage as GenericDrawPage
from ...lo.drawing.generic_drawing_document import GenericDrawingDocument as GenericDrawingDocument
from ...lo.drawing.glue_point import GluePoint as GluePoint
from ...lo.drawing.glue_point2 import GluePoint2 as GluePoint2
from ...lo.drawing.gradient_table import GradientTable as GradientTable
from ...lo.drawing.graphic_export_filter import GraphicExportFilter as GraphicExportFilter
from ...lo.drawing.graphic_filter_request import GraphicFilterRequest as GraphicFilterRequest
from ...lo.drawing.graphic_object_shape import GraphicObjectShape as GraphicObjectShape
from ...lo.drawing.group_shape import GroupShape as GroupShape
from ...lo.drawing.hatch import Hatch as Hatch
from ...lo.drawing.hatch_style import HatchStyle as HatchStyle
from ...lo.drawing.hatch_table import HatchTable as HatchTable
from ...lo.drawing.homogen_matrix import HomogenMatrix as HomogenMatrix
from ...lo.drawing.homogen_matrix3 import HomogenMatrix3 as HomogenMatrix3
from ...lo.drawing.homogen_matrix4 import HomogenMatrix4 as HomogenMatrix4
from ...lo.drawing.homogen_matrix_line import HomogenMatrixLine as HomogenMatrixLine
from ...lo.drawing.homogen_matrix_line3 import HomogenMatrixLine3 as HomogenMatrixLine3
from ...lo.drawing.homogen_matrix_line4 import HomogenMatrixLine4 as HomogenMatrixLine4
from ...lo.drawing.horizontal_dimensioning import HorizontalDimensioning as HorizontalDimensioning
from ...lo.drawing.layer import Layer as Layer
from ...lo.drawing.layer_manager import LayerManager as LayerManager
from ...lo.drawing.layer_type import LayerType as LayerType
from ...lo.drawing.line_cap import LineCap as LineCap
from ...lo.drawing.line_dash import LineDash as LineDash
from ...lo.drawing.line_end_type import LineEndType as LineEndType
from ...lo.drawing.line_joint import LineJoint as LineJoint
from ...lo.drawing.line_properties import LineProperties as LineProperties
from ...lo.drawing.line_shape import LineShape as LineShape
from ...lo.drawing.line_style import LineStyle as LineStyle
from ...lo.drawing.marker_table import MarkerTable as MarkerTable
from ...lo.drawing.master_page import MasterPage as MasterPage
from ...lo.drawing.master_pages import MasterPages as MasterPages
from ...lo.drawing.measure_kind import MeasureKind as MeasureKind
from ...lo.drawing.measure_properties import MeasureProperties as MeasureProperties
from ...lo.drawing.measure_shape import MeasureShape as MeasureShape
from ...lo.drawing.measure_text_horz_pos import MeasureTextHorzPos as MeasureTextHorzPos
from ...lo.drawing.measure_text_vert_pos import MeasureTextVertPos as MeasureTextVertPos
from ...lo.drawing.mirror_axis import MirrorAxis as MirrorAxis
from ...lo.drawing.module_dispatcher import ModuleDispatcher as ModuleDispatcher
from ...lo.drawing.normals_kind import NormalsKind as NormalsKind
from ...lo.drawing.ole2_shape import OLE2Shape as OLE2Shape
from ...lo.drawing.open_bezier_shape import OpenBezierShape as OpenBezierShape
from ...lo.drawing.page_shape import PageShape as PageShape
from ...lo.drawing.plugin_shape import PluginShape as PluginShape
from ...lo.drawing.point_sequence import PointSequence as PointSequence
from ...lo.drawing.point_sequence_sequence import PointSequenceSequence as PointSequenceSequence
from ...lo.drawing.poly_line_shape import PolyLineShape as PolyLineShape
from ...lo.drawing.poly_polygon_bezier_coords import PolyPolygonBezierCoords as PolyPolygonBezierCoords
from ...lo.drawing.poly_polygon_bezier_descriptor import PolyPolygonBezierDescriptor as PolyPolygonBezierDescriptor
from ...lo.drawing.poly_polygon_bezier_shape import PolyPolygonBezierShape as PolyPolygonBezierShape
from ...lo.drawing.poly_polygon_descriptor import PolyPolygonDescriptor as PolyPolygonDescriptor
from ...lo.drawing.poly_polygon_shape import PolyPolygonShape as PolyPolygonShape
from ...lo.drawing.poly_polygon_shape3_d import PolyPolygonShape3D as PolyPolygonShape3D
from ...lo.drawing.polygon_flags import PolygonFlags as PolygonFlags
from ...lo.drawing.polygon_kind import PolygonKind as PolygonKind
from ...lo.drawing.position3_d import Position3D as Position3D
from ...lo.drawing.projection_mode import ProjectionMode as ProjectionMode
from ...lo.drawing.rectangle_point import RectanglePoint as RectanglePoint
from ...lo.drawing.rectangle_shape import RectangleShape as RectangleShape
from ...lo.drawing.rotation_descriptor import RotationDescriptor as RotationDescriptor
from ...lo.drawing.shade_mode import ShadeMode as ShadeMode
from ...lo.drawing.shading_pattern import ShadingPattern as ShadingPattern
from ...lo.drawing.shadow_properties import ShadowProperties as ShadowProperties
from ...lo.drawing.shape import Shape as Shape
from ...lo.drawing.shape_collection import ShapeCollection as ShapeCollection
from ...lo.drawing.shapes import Shapes as Shapes
from ...lo.drawing.slide_renderer import SlideRenderer as SlideRenderer
from ...lo.drawing.slide_sorter import SlideSorter as SlideSorter
from ...lo.drawing.snap_object_type import SnapObjectType as SnapObjectType
from ...lo.drawing.text import Text as Text
from ...lo.drawing.text_adjust import TextAdjust as TextAdjust
from ...lo.drawing.text_animation_direction import TextAnimationDirection as TextAnimationDirection
from ...lo.drawing.text_animation_kind import TextAnimationKind as TextAnimationKind
from ...lo.drawing.text_fit_to_size_type import TextFitToSizeType as TextFitToSizeType
from ...lo.drawing.text_horizontal_adjust import TextHorizontalAdjust as TextHorizontalAdjust
from ...lo.drawing.text_properties import TextProperties as TextProperties
from ...lo.drawing.text_shape import TextShape as TextShape
from ...lo.drawing.text_vertical_adjust import TextVerticalAdjust as TextVerticalAdjust
from ...lo.drawing.texture_kind import TextureKind as TextureKind
from ...lo.drawing.texture_kind2 import TextureKind2 as TextureKind2
from ...lo.drawing.texture_mode import TextureMode as TextureMode
from ...lo.drawing.texture_projection_mode import TextureProjectionMode as TextureProjectionMode
from ...lo.drawing.transparency_gradient_table import TransparencyGradientTable as TransparencyGradientTable
from ...lo.drawing.vertical_dimensioning import VerticalDimensioning as VerticalDimensioning
from ...lo.drawing.x_connectable_shape import XConnectableShape as XConnectableShape
from ...lo.drawing.x_connector_shape import XConnectorShape as XConnectorShape
from ...lo.drawing.x_control_shape import XControlShape as XControlShape
from ...lo.drawing.x_custom_shape_engine import XCustomShapeEngine as XCustomShapeEngine
from ...lo.drawing.x_custom_shape_handle import XCustomShapeHandle as XCustomShapeHandle
from ...lo.drawing.x_draw_page import XDrawPage as XDrawPage
from ...lo.drawing.x_draw_page_duplicator import XDrawPageDuplicator as XDrawPageDuplicator
from ...lo.drawing.x_draw_page_expander import XDrawPageExpander as XDrawPageExpander
from ...lo.drawing.x_draw_page_summarizer import XDrawPageSummarizer as XDrawPageSummarizer
from ...lo.drawing.x_draw_page_supplier import XDrawPageSupplier as XDrawPageSupplier
from ...lo.drawing.x_draw_pages import XDrawPages as XDrawPages
from ...lo.drawing.x_draw_pages_supplier import XDrawPagesSupplier as XDrawPagesSupplier
from ...lo.drawing.x_draw_sub_controller import XDrawSubController as XDrawSubController
from ...lo.drawing.x_draw_view import XDrawView as XDrawView
from ...lo.drawing.x_enhanced_custom_shape_defaulter import XEnhancedCustomShapeDefaulter as XEnhancedCustomShapeDefaulter
from ...lo.drawing.x_glue_points_supplier import XGluePointsSupplier as XGluePointsSupplier
from ...lo.drawing.x_graphic_export_filter import XGraphicExportFilter as XGraphicExportFilter
from ...lo.drawing.x_layer import XLayer as XLayer
from ...lo.drawing.x_layer_manager import XLayerManager as XLayerManager
from ...lo.drawing.x_layer_supplier import XLayerSupplier as XLayerSupplier
from ...lo.drawing.x_master_page_target import XMasterPageTarget as XMasterPageTarget
from ...lo.drawing.x_master_pages_supplier import XMasterPagesSupplier as XMasterPagesSupplier
from ...lo.drawing.x_presenter_helper import XPresenterHelper as XPresenterHelper
from ...lo.drawing.x_selection_function import XSelectionFunction as XSelectionFunction
from ...lo.drawing.x_shape import XShape as XShape
from ...lo.drawing.x_shape_aligner import XShapeAligner as XShapeAligner
from ...lo.drawing.x_shape_arranger import XShapeArranger as XShapeArranger
from ...lo.drawing.x_shape_binder import XShapeBinder as XShapeBinder
from ...lo.drawing.x_shape_combiner import XShapeCombiner as XShapeCombiner
from ...lo.drawing.x_shape_descriptor import XShapeDescriptor as XShapeDescriptor
from ...lo.drawing.x_shape_group import XShapeGroup as XShapeGroup
from ...lo.drawing.x_shape_grouper import XShapeGrouper as XShapeGrouper
from ...lo.drawing.x_shape_mirror import XShapeMirror as XShapeMirror
from ...lo.drawing.x_shapes import XShapes as XShapes
from ...lo.drawing.x_shapes2 import XShapes2 as XShapes2
from ...lo.drawing.x_shapes3 import XShapes3 as XShapes3
from ...lo.drawing.x_slide_preview_cache import XSlidePreviewCache as XSlidePreviewCache
from ...lo.drawing.x_slide_preview_cache_listener import XSlidePreviewCacheListener as XSlidePreviewCacheListener
from ...lo.drawing.x_slide_renderer import XSlideRenderer as XSlideRenderer
from ...lo.drawing.x_slide_sorter_base import XSlideSorterBase as XSlideSorterBase
from ...lo.drawing.x_universal_shape_descriptor import XUniversalShapeDescriptor as XUniversalShapeDescriptor
